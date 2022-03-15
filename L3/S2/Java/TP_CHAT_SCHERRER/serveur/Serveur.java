/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */

package serveur;

import java.awt.Color;
import java.awt.Dimension;

import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import java.net.ServerSocket;
import java.net.Socket;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

import java.util.concurrent.CopyOnWriteArrayList;

import javax.swing.JFrame;



/**
 * La classe Serveur permet de gérer le serveir et la fenêtre du serveur
 * 
 *  Les VI de la classe sont :::
 * 
 *      - serialVersionUID  ==> variable pour la serialisation
 *      - port              ==> constante correspondant au port sur lequel il faut se connecter
 *      - fenêtre           ==> fenêtre du serveur
 *      - listeConnectes    ==> liste des utilisateurs connectés
 *      - file              ==> fichier contenant la liste des utilisateurs en ligne
 *      - nbConnexions      ==> nombre d'utilisateurs connectés
 */
public class Serveur extends JFrame {


    static final int port = 80;
    private static FenetreServeur fenetre;
    private static List<String> listeConnectes = new ArrayList<>();
    private static CopyOnWriteArrayList<ServeurThread> listeThread = new CopyOnWriteArrayList<>();
    private static List<String> discussion;
    private static File file;
    private static int nbConnexions;



    /**
     * Constructeur pour creer un Serveur
     *
     * @param port numero de port du serveur
     */
    public Serveur(int port) {
        super("Gestion du serveur");
        initialiser();

        nbConnexions = 0;

        discussion = new ArrayList<>();
        file = new File("utilisateurs.txt");

        if(file.exists()) {
            file.delete();
        }

        try {
            file.createNewFile();
        } catch(IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Méthode permettant de lancer le serveur
     */
    public void lancer() {
        try (ServerSocket serveur = new ServerSocket(port)) {

            while (true) {

                Socket socketClient = serveur.accept();
                fenetre.setStatut("Serveur en route sur le port " + Serveur.port + " (nb de connexions = " + nbConnexions + ")");

                // Creation d'un nouveau objet thread
                ServeurThread connexion = new ServeurThread(socketClient);
                // Ajout du nouveau thread a la liste
                listeThread.add(connexion);
                connexion.start();
            }

        } catch(IOException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Classe interne permettant de lire les messages
     * @see Thread
     */
    private static class ServeurThread extends Thread {

        private final Socket socket;
        private DataOutputStream output;
        private Utilisateur utilisateur;

        /**
         * Constructeur pour creer un ServeurThread
         * @param socket socket
         */
        public ServeurThread(Socket socket) {
            this.socket = socket;
        }

        // ********************* //
        // ****** GETTERS ****** //
        // ********************* //

        /**
         * Getter de l'utilisateur actuel
         * @return l'utilisateur
         */
        public Utilisateur getUtilisateur() {
            return utilisateur;
        }

        /**
         *  redéfinition de la méthode qui est executée par le ServeurThread
         * @see Thread
         */
        @Override
        public void run() {
            try {
                output = new DataOutputStream(socket.getOutputStream());
                DataInputStream input = new DataInputStream(socket.getInputStream());
                utilisateur = new Utilisateur(input.readUTF());

                String messageClient = "";
                String messageServeur = "";

                // Ajout de l'utilisateur a la liste s'il n'y est pas deja
                if(!listeConnectes.contains(utilisateur.getNom())) {
                    listeConnectes.add(utilisateur.getNom());
                }

                // Ajout de l'utilisateur dans le file (sa couleur est generée et ajoutée)
                ajouterUtilisateurDansFichier(utilisateur);

                envoyerListeBroadcast();

                // Tant que le client ne s'est pas deconnecté, le serveur lit les messages
                do {
                    messageClient = input.readUTF();
                    System.out.println("Message recu => " + messageClient);

                    StringTokenizer tokenizer = new StringTokenizer(messageClient, "-");
                    String option = tokenizer.nextToken();

                    // Si le prefixe est "chat" : message a envoyé a tous les utilisateurs
                    if(option.equals("chat")) {
                        option = tokenizer.nextToken();

                        // Gestion de la déconnexion
                        if(messageClient.contains("Déconnexion")) {
                            messageServeur = utilisateur.getNom() + " s'est déconnecté.";
                            // Envoi du message a tout le monde sauf la personne qui s'est deconnecté
                            envoyerBroadcast(messageServeur, utilisateur.getNom());
                        } else {
                            // Ajout de l'expéditeur devant le message
                            messageServeur = utilisateur.getNom() + " : " + option;
                            envoyerBroadcast(messageServeur, null);
                        }
                    }
                    // Si le prefixe est "privé" : message prive
                    else if(option.equals("prive")) {
                        // récuperation du nom du destinatire
                        String destinataire = tokenizer.nextToken();
                        option = tokenizer.nextToken();
                        messageServeur = utilisateur.getNom() + " (" + destinataire + ") : " + option;
                        envoyerMessagePrive(messageServeur, utilisateur.getNom(), destinataire);
                    }

                    System.out.println("Message serveur =>  " + messageServeur);
                    ajouterMessageDansDiscussion(messageServeur);
                } while (!messageClient.contains("Deconnexion"));

                supprimerUtilisateur(this);

                envoyerListeBroadcast();

            } catch(IOException e) {
                e.printStackTrace();
            } catch(Exception e) {
                e.printStackTrace();
            }
        }

        /**
         * Méthode permettant a un client d'envoyer un message a toutes les personnes
         * @param message message à envoyer
         */
        public void envoyerMessage(String message) {
            try {
                output.writeUTF(message);
            } catch(IOException e) {
                System.out.println("Erreur lors de l'envoi");
                e.printStackTrace();
            }
        }

        /**
         * Méthode permettant d'envoyer a toutes les personnes connectees au serveur la liste des personnes connectees
         */
        public void envoyerListeBroadcast() {
            if(!listeThread.isEmpty()) {
                String s = String.join("-", listeConnectes);
                envoyerBroadcast("init-" + s, null);
                System.out.println("Liste utilisateurs envoyee : " + s + ",");
            } else {
                System.out.println("Liste utilisateurs non envoyee");
            }
        }
    }

    /**
     * Méthode d'initialisation l'affichage de la fenetre du serveur
     */
    public void initialiser() {
        fenetre = new FenetreServeur();
        add(fenetre);

        fenetre.setStatut("En attente de connexion...");

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        setSize(new Dimension(420, 600)); 
        setLocationRelativeTo(null);

        addWindowListener(new WindowAdapter() {
            /**
             * Méthode qui est executee en cas de fermeture de la fenetre
             * @param e evenement
             */
            @Override
            public void windowClosed(WindowEvent e) {
                if(file.exists()) {
                    file.delete();
                }
            }
        });
        setVisible(true);
    }

    /**
     * Méthode permettant d'ajouter un nouvel utilisateur dans le file
     * @param u utilisateur a ajouter
     */
    public static void ajouterUtilisateurDansFichier(Utilisateur u) {

        // On verifie que l'utilisateur ne s'est pas déjà connecté une fois
        if(utilisateurPresent(u.getNom())) {
            
            Color couleur = u.genererCouleur();
            u.setCouleur(couleur);
            ecrireDansFichier(u);
        }
        u.setConnecte(true);

        fenetre.ajouterUtilisateurFenetre(u.getNom());
        System.out.println("Nouveau utilisateur ajoute avec succes : " + u.getNom());
        nbConnexions++;
        fenetre.setStatut("Serveur en route sur le port " + Serveur.port + " (nb de connexions = " + nbConnexions + ")");
    }

    /**
     * Méthode permettant de supprimer le thread d'un utilisateur qui s'est deconnecte
     * @param st thread a supprimer de la liste
     */
    public static void supprimerUtilisateur(ServeurThread st) {
        listeConnectes.remove(st.getUtilisateur().getNom());
        st.getUtilisateur().setConnecte(false);
        listeThread.remove(st);
        majAffichageConnectes();

        nbConnexions--;
        fenetre.setStatut("Serveur en route sur le port " + Serveur.port + " (nb de connexions = " + nbConnexions + ")");
    }

    /**
     * Méthode permettant de mettre à jour l'affichage de la liste des personnes connectees
     */
    public static void majAffichageConnectes() {
        fenetre.effacerUtilisateursFenetre(); 

        for (ServeurThread st : listeThread) {
            if(st.getUtilisateur().getConnecte()) {
                fenetre.ajouterUtilisateurFenetre(st.getUtilisateur().getNom());
            }
        }
    }

    /**
     * Méthode permettant d'ecrire dans le file .txt les noms des utilisateurs ainsi que leur couleur associee
     * @param u utilisateur a ajouter
     */
    public static void ecrireDansFichier(Utilisateur u) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(file, true))) {
            String s = u.getNom() + ":" + u.getCouleur();
            writer.write(s);
            writer.newLine(); 

            System.out.println("\t=> Ajout de l'utilisateur dans le file  : "+s);
        } catch(IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Méthode permettant d'envoyer un message a tous les utilisateurs sauf a l'expediteur. Si l'expediteur == null, tout le monde reçoit le message
     * @param msg        message à envoyer
     * @param expediteur expediteur du message
     */
    public static void envoyerBroadcast(String msg, String expediteur) {
        for (ServeurThread utilisateur : listeThread) {
            if((expediteur==null) || (!utilisateur.getUtilisateur().getNom().equals(expediteur))) {
                utilisateur.envoyerMessage(msg);
            }
        }
    }

    /**
     * Méthode permettant d'envoyer le message uniquement a l'expediteur et au destinataire (message prive)
     * @param msg message a envoyer
     * @param expediteur expediteur du message
     * @param destinataire destinatire du message
     */
    public static void envoyerMessagePrive(String msg, String expediteur, String destinataire) {
        for (ServeurThread utilisateur : listeThread) {
            if(utilisateur.getUtilisateur().getNom().equals(expediteur) || utilisateur.getUtilisateur().getNom()
                    .equals(destinataire)) {
                utilisateur.envoyerMessage(msg);
            }
        }
    }

    /**
     * Méthode permettant de savoir si un utilisateur donne est deja present dans la liste
     * @param nom nom de l'utilisateur pour lequel on veut verifier sa presence ou non
     * @return un booleen
     */
    public static boolean utilisateurPresent(String nom) {
        for(int i = 0; i < listeConnectes.size(); i++) {
            if(listeConnectes.get(i).equals(nom)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Méthode permettant d'ajouter un message dans la discussion
     * @param msg nouveau message a ajouter
     */
    public static void ajouterMessageDansDiscussion(String msg) {
        discussion.add(msg + "\n");
        fenetre.getDiscussion().append(msg + "\n");
    }
}

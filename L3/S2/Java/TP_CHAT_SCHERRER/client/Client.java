/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */

package client;

import java.awt.Color;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;

import java.net.ConnectException;
import java.net.NoRouteToHostException;
import java.net.Socket;
import java.net.UnknownHostException;

import java.util.Map;
import java.util.StringTokenizer;

import javax.swing.JOptionPane;
import javax.swing.JTextPane;

import javax.swing.text.AttributeSet;
import javax.swing.text.BadLocationException;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import javax.swing.text.StyledDocument;

/**
 * La classe Client permet de gérer les données rentrées par l'utilisateur lorsqu'il veut se connecter
 * 
 *  Les VI de la classe Client sont :::
 *    
 *      - fenetre   ==> une fenêtre 
 *      - nom       ==> nom du client
 *      - port      ==> numéro du port
 *      - ip        ==> adresse IP
 *      - isConnecte  ==> booleen permettant de savoir si le client est connecté
 *      - output    ==> sortie du client
 *      - input     ==> entree du client
 *      - socket    ==> socket du client 
 */
  
public class Client {

    private FenetreClient fenetre;
    private String nom;
    private int port;
    private String ip;
    private boolean isConnecte;
    private DataOutputStream output;
    private DataInputStream input;
    private Socket socket;

    /**
     * Constructeur de la classe Client
     *
     * @param f    la fenêtre du client
     * @param nom  nom du client
     * @param ip   adresse IP
     * @param port numero du port servant à la connexion avec le serveur
     */
    public Client(FenetreClient f, String nom, String ip, int port) {
        this.nom = nom;
        this.ip = ip;
        this.port = port;
        this.fenetre = f;
        this.isConnecte = false; // l'utilisateur est déconnecté par défaut
    }

    // ***************************************** //
    // ****** GETTERS DE LA CLASSE CLIENT ****** //
    // ***************************************** //

    /**
     * Getter du nom du client
     * @return le nom du client
     */
    public String getNom() {
        return nom;
    }

    /**
     * Getter du boolean isConnecte
     * @return un booleen
     */
    public boolean getConnecte() {
        return isConnecte;
    }

    /**
     * Méthode permettant au client de se connecter au serveur
     */
    public void connexion() {
        if(connexionServeur(ip)) {
            isConnecte = true;
            System.out.println("Connexion OK");
            new LectureMessageThread().start(); // nouveau thread pour lire les messages
        }
    }

    /**
     * Méthode qui renvoie true si la connexion avec le serveur s'est bien passé 
     *
     * @param hote hote
     * @return true si la connexion est un succès
     */
    public boolean connexionServeur(String hote) {
        try {
            socket = new Socket(hote, port);
            input = new DataInputStream(socket.getInputStream());
            output = new DataOutputStream(socket.getOutputStream());

            // Envoi du nom du client au serveur
            output.writeUTF(this.nom);

        } catch(UnknownHostException e) {
            JOptionPane.showMessageDialog(fenetre, "Adresse IP inconnue", "Erreur", JOptionPane.ERROR_MESSAGE);
            return false;

        } catch(ConnectException e) {
            JOptionPane.showMessageDialog(fenetre, "Le serveur ne doit pas être lancé :(", "Erreur", JOptionPane.ERROR_MESSAGE);
            return false;

        } catch(NoRouteToHostException e) {
            JOptionPane.showMessageDialog(fenetre, "Hote introuvable", "Erreur", JOptionPane.ERROR_MESSAGE);
            return false;

        } catch(IOException ex) {
            ex.printStackTrace();
            System.out.println("Erreur avec la connexion au serveur");
        }
        return true;
    }

    /**
     * Méthode qui déconnecte le client
     */
    public void deconnexion() {
        envoyerMessage("Déconnexion","Tout le monde");

        isConnecte = false; // maj du statut du client 
        System.out.println("Déconnexion réussie");
    }

    /**
     * Méthode permettant d'envoyer un message
     *
     * @param message  message à envoyer
     * @param destinataire options d'envoi (tout le monde ou un utilisateur donné)
     */
    public void envoyerMessage(String message, String destinataire) {
        JTextPane jtp = fenetre.getPanneauDiscussion().getDiscussion();

        try {
            String str= "";

            // L'utilisateur décide d'envoyer un message à une personne en particulier
            if(!destinataire.equals("Tout le monde")) {
                
                str = "prive-"+ destinataire + "-" + message + "-"; // on précise au serveur qu'il s'agit d'un message privé
                System.out.println("Message privé envoyé : " + message);
            }

            // L'utilisateur décide d'envoyer le message à tout le monde
            else {
                str = "chat-" + message + "-"; // on précise au serveur qu'il faut envoyer le message à tous les utilisateurs
                System.out.println("Message envoyé : " + message);
            }
            output.writeUTF(str); // envoie du message

        } catch(Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
            jtp.setText(jtp.getText().concat("\nErreur : le message n'a pas pu s'envoyer :("));
        }
    }

    /**
     * Classe interne pour lire les messages entrants
     */
    private class LectureMessageThread extends Thread {
        /**
         * Méthode executée dans le Thread
         */
        @Override
        public void run() {
            
            // Tant que le client est connecté, les messages peuvent être lus
            while (isConnecte) {
                String message = "";
                StyledDocument sd = fenetre.getPanneauDiscussion().getDiscussion().getStyledDocument();

                try {
                    if(isConnecte) {
                        message = input.readUTF();

                        
                        StringTokenizer sTokenizer = new StringTokenizer(message, "-"); // découpage de la chaine avec un délimiteur
                        String option = sTokenizer.nextToken();

                        // Si le message contient "init", le serveur envoie la liste des personnes connectees
                        // Ce message est envoyé uniquement lors d'une nouvelle connexion ou d'une deconnexion d'un utilisateur au serveur
                        if(option.contains("init")) {

                            fenetre.getPanneauDiscussion().videListeClient();

                            while (sTokenizer.hasMoreTokens()) {
                                option = sTokenizer.nextToken();
                                fenetre.getPanneauDiscussion().ajouterClientListe(option);
                            }

                            fenetre.getPanneauDiscussion().majAffichageConnectes();
                        }

                        // Cas d'un message privé
                        else if(option.contains("(")) {
                            int i = message.indexOf("(");
                            String nom = message.substring(0, i-1); // récupération du nom

                            System.out.println("Message privé reçu : " + message);

                            // Ajout du message dans le panneau de discussion
                            ajouterMessage(sd, StyleContext.getDefaultStyleContext(), StyleConstants.Foreground, chercherCouleur(nom), message);
                        }

                        // Cas d'un message broadcast
                        else {
                            String[] tmp = (message.split(" : "));
                            String nom = tmp[0]; // recuperation du nom

                            System.out.println("Message recu : " + message);

                            if(!message.contains("deconnecté")) {
                                // Le message prend la couleur correspondant à la personne qui l'a envoyé
                                ajouterMessage(sd, StyleContext.getDefaultStyleContext(), StyleConstants.Foreground, chercherCouleur(nom), message);
                            }

                            // Gestion des messages de déconnexion des autres utilisateurs
                            else {
                                ajouterMessage(sd, StyleContext.getDefaultStyleContext(), StyleConstants.Italic, true, message);
                            }
                        }

                    } 
                } catch(Exception e) {
                    System.out.println(e.getMessage());
                    e.printStackTrace();
                }
            } 
        }
    }

    /**
     * Méthode permettant d'inserer un message avec une couleur ou un style donne
     *
     * @param sd      StyledDocument
     * @param sc      StyleContext
     * @param name    Nom de la constante
     * @param value   valeur
     * @param message message a ajouter
     */
    public void ajouterMessage(StyledDocument sd, StyleContext sc, Object name, Object value, String message) {
        StyledDocument doc = sd;
        StyleContext style = sc;

        // Affectation de la couleur ou du style donné en argument
        AttributeSet att = style.addAttribute(style.getEmptySet(), name, value);

        AttributeSet aset = null;

        // Si le message est privé, on ajoute de la couleur et l'attribut "italique"
        if(message.contains("(")) {
            aset = style.addAttributes(att, style.addAttribute(style.getEmptySet(), StyleConstants.Italic, true));
        } else {
            aset = style.addAttributes(att, style.addAttribute(style.getEmptySet(), StyleConstants.Bold, true));
        }

        try {
            doc.insertString(doc.getLength(), message + "\n", aset);
            
            fenetre.getPanneauDiscussion().getDiscussion().setCaretPosition(fenetre.getPanneauDiscussion().getDiscussion().getDocument().getLength()); // Gestion de l'auto-scrolling
        } catch(BadLocationException e) {
            e.printStackTrace();
        }
    }

    /**
     * Méthode permettant de chercher la couleur correspondant à une personne
     * @param nom nom de la personne pour qui on cherche sa couleur
     * @return la couleur (format rgb = un entier)
     */
    public Color chercherCouleur(String nom) {
        PanneauDiscussion p = fenetre.getPanneauDiscussion();

        for (Map.Entry<String, Color> entry : p.getCouleurs().entrySet()) {
            if(entry.getKey().equals(nom)) {
                return entry.getValue(); 
            }
        }
        return Color.BLACK;
    }
}
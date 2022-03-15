/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */

package client;
import javax.swing.JFrame;

import java.awt.Dimension;
import java.awt.BorderLayout;
import java.awt.EventQueue;

import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;


/**
 * La classe FenetreClient hérite de JFrame. Elle va gérer le rendu graphique de l'interface du client
 * 
 *  Les VI de la classe FenetreCient sont :::
 *      
 *      - panneauConnexion      ==> zone réservée au formulaire de connexion
 *      - panneauDiscussion     ==> zone réservée à la discussion
 *      - client                ==> client de la fenêtre
 */
public class FenetreClient extends JFrame {

    private PanneauConnexion panneauConnexion;
    private PanneauDiscussion panneauDiscussion;
    private Client client;

    
    /**
     * Constructeur de la classe FenetreClient
     */
    public FenetreClient() {

        super("Chat en Ligne");
        this.setLayout(new BorderLayout(10, 10));

        this.panneauConnexion = new PanneauConnexion(this);
        this.panneauDiscussion = new PanneauDiscussion(this);
        this.add(panneauConnexion, BorderLayout.NORTH);
        this.add(panneauDiscussion, BorderLayout.CENTER);
        cacherDiscussion(); // tant que le client n'est pas connecté

        this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE); 

        // Si le client ferme la fenêtre sans s'être déconnecté, alors on le deconnecte
        addWindowListener(new WindowAdapter() {
            /**
             * Méthode qui est executee en cas de fermeture de la fenetre
             */
            @Override
            public void windowClosed(WindowEvent e) {
                if((client != null) && client.getConnecte()) {
                    client.deconnexion();
                }
            }
        });

        this.setSize(new Dimension(540, 700));
        this.setLocationRelativeTo(null);
        this.setVisible(true);
    }


    // ************************************************ //
    // ****** GETTERS DE LA CLASSE FENETRECLIENT ****** //
    // ************************************************ //
    /**
     * Getter pour le panneau de discussion
     * @return le panneau de discussion
     */
    public PanneauDiscussion getPanneauDiscussion() {
        return panneauDiscussion;
    }

    /**
     * Getter du client de la fenetre
     * @return le client de la fenetre
     */
    public Client getClient() {
        return client;
    }

    // ************************************************ //
    // ****** SETTERS DE LA CLASSE FENETRECLIENT ****** //
    // ************************************************ //
    /**
     * Permet d'affecter un nouveau client a la fenetre
     * @param client le client à affecter à la fenetre
     */
    public void setClient(Client client) {
        this.client = client;
    }


    /**
     * Méthode permettant d'afficher le panneau de discussion
     */
    public void afficherDiscussion() {
        panneauDiscussion.setVisible(true);
    }

    /**
     * Méthode permettant de cacher le panneau de discussion
     */
    public void cacherDiscussion() {
        panneauDiscussion.setVisible(false);
    }

    /**
     * Méthode permettant d'effacer la discussion
     */
    public void effacerDiscussion() {
        panneauDiscussion.effacerDiscussion();
    }

    

    /**
     * Programme prinicpal
     * @param args arguments de la ligne de commande
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            /**
             * Redéfinition de ma méthode run
             */
            @Override
            public void run() {
                new FenetreClient();
            }
        });
    }
}
/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */

package client;

import java.awt.BorderLayout;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JTextField;

import javax.swing.border.EmptyBorder;

import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;

/**
 * La classe PanneauConnexion hérite de JPanel. Elle représente la zone de connexion du client
 * 
 *  Les VI de cette classe sont :::
 * 
 *      - nameField     ==> panneau pour la saisie du nom du client
 *      - ipField       ==> panneau pour la saisie de l'IP du client
 *      - portField     ==> panneau pour la saisie du port du client
 *      - button        ==> boutton pour se connecter
 *      - tabFields     ==> tableau de 3 zones de textes servant à l'utilisteur pour se connecter
 *      - fenetre       ==> fenêtre du client
 */
public class PanneauConnexion extends JPanel {

    private SaisieConnexion nameField;
    private SaisieConnexion ipField;
    private SaisieConnexion portField;
    private JButton button;
    private JTextField[] tabFields;
    private FenetreClient fenetre;

    /**
     * Constructeur de la classe PanneauConnexion
     * @param f fenetre du client
     */
    public PanneauConnexion(FenetreClient f) {
        this.fenetre = f;

        // Zones de connexion
        this.nameField = new SaisieConnexion("Nom");
        this.ipField = new SaisieConnexion("IP");
        this.portField = new SaisieConnexion("Port");


        this.tabFields = new JTextField[3];
        tabFields[0] = nameField.getTextField();
        tabFields[1] = ipField.getTextField();
        tabFields[2] = portField.getTextField();

        for (JTextField field : tabFields)
            field.getDocument().addDocumentListener(new FieldListener());

        this.button = new JButton("Connexion");

        // Ajout d'un listener sur le bouton
        button.addActionListener(new ActionListener() {
            /**
             * Méthode qui va être appelée quand le client va cliquer sur le bouton
             * 'Connexion' ou 'Déconnexion'
             *
             * @param e evenement
             */
            @Override
            public void actionPerformed(ActionEvent e) {

                // Le client veut se connecter
                if(button.getText().equals("Connexion")) {
                    for (JTextField field : tabFields)
                        field.setEnabled(false); 
                    button.setText("Déconnexion");

                    fenetre.afficherDiscussion();

                    fenetre.setClient(new Client(fenetre, getNom(), getIP(), Integer.parseInt(getPort())));
                    System.out.println("Nouveau client : " + getNom());

                    fenetre.getClient().connexion();
                }
                
                // Le client veut se déconnecter 
                else {
                    fenetre.getClient().deconnexion();
                    fenetre.setClient(null); 

                    fenetre.effacerDiscussion();
                    fenetre.cacherDiscussion();

                    for (JTextField field : tabFields)
                        field.setEnabled(true); // les zones de saisie pour la connexion sont de nouveau accessible

                    button.setText("Connexion");
                }
            }
        });

        //Gestion de la partie gauche
        JPanel gauche = new JPanel(new BorderLayout(5, 5));
        gauche.add(nameField, BorderLayout.NORTH);
        gauche.add(ipField, BorderLayout.SOUTH);
        button.setEnabled(false); // griser le bouton

        //Gestion de la partie droite
        JPanel droit = new JPanel(new BorderLayout(5, 5));
        droit.add(button, BorderLayout.NORTH);
        droit.add(portField, BorderLayout.SOUTH);

        this.setLayout(new BorderLayout());
        this.setBorder(new EmptyBorder(6, 6, 6, 6));
        this.add(gauche, BorderLayout.WEST);
        this.add(droit, BorderLayout.EAST);
    }

    // **************************************************** //
    // ****** GETTERS DE LA CLASSE PANNEAUCONNEXION ******* //
    // **************************************************** //

    /**
     * Getter de l'IP saisi par le client
     * @return l'adresse IP
     */
    public String getIP() {
        return ipField.getSaisie();
    }

    /**
     * Getter du numero de port saisi par le client
     * @return le numero de port saisi
     */
    public String getPort() {
        return portField.getSaisie();
    }

    /**
     * Getter du nom du client
     * @return le nom du client
     */
    public String getNom() {
        return nameField.getSaisie();
    }




    /**
     * Classe interne pour gerer les listeners des zones de textes
     */
    private class FieldListener implements DocumentListener {
        
        /**
         * Méthode permettant de savoir si quelque chose a été ajouté au document
         * @param e evenement
         */
        @Override
        public void insertUpdate(DocumentEvent e) {
            verifierSaisie();
        }

        /**
         * Méthode permettant de savoir si quelque chose a été supprimé du document
         * @param e evenement
         */
        @Override
        public void removeUpdate(DocumentEvent e) {
            verifierSaisie();
        }

        /**
         * Méthode permettant de savoir s'il y eu des changements
         * @param e evenement
         */
        @Override
        public void changedUpdate(DocumentEvent e) {
            verifierSaisie();
        }

        /**
         * Méthode permettant de verifier que le client a bien rempli tous les champs de connexion
         */
        public void verifierSaisie() {
            boolean ok = true;

            for(JTextField field : tabFields)
                if(field.getText().trim().equals(""))
                    ok = false;
            // Pour que le bouton de connexion soit dispo, il faut que le client ait rempli tous les champs
            if(ok)
                button.setEnabled(true);
            else
                button.setEnabled(false);
        }
    }

    
}

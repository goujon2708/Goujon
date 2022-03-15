/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */


package serveur;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import javax.swing.border.EmptyBorder;

import java.awt.BorderLayout;


/**
 * La classe FenetreServeur herite de JPanel La classe FenetreServeur gere l'affichage sur la fenetre du serveur.
 * La FenetreServeur est constituee de :
 * - une zone pour afficher les users
 * - une zone pour afficher la discussion
 * - un statut
 */

/**
 * La classe FenetreServeur gère l'affichage sur la fenêtre du serveur
 * 
 *  Les VI de la classe sont :::
 *      
 *      - users      ==> zone listant les users
 *      - discussion        ==> zone montrant la discussion
 *      - statut            ==> zone montrant le statur des participants
 */
public class FenetreServeur extends JPanel {

    private JTextArea users;
    private JTextArea discussion;
    private JLabel statut;

    /**
     * Constructeur de la classe FenetreServeur
     */
    public FenetreServeur() {
        this.statut = new JLabel();
        this.users = new JTextArea(10,35);
        this.discussion = new JTextArea(17,35);
        this.discussion.setLineWrap(true);



        JScrollPane scrollDis = new JScrollPane(discussion);
        scrollDis.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        
        JScrollPane scrollUtil = new JScrollPane(users);
        scrollUtil.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        // les zones pour afficher les users et la discussion ne doivent pas être editables
        this.users.setEditable(false);
        this.discussion.setEditable(false);

        // Gestion du panneau avec les users du serveur
        JPanel panelUtil = new JPanel(new BorderLayout(5,5));
        panelUtil.add(new JLabel("Utilisateurs"), BorderLayout.NORTH);
        panelUtil.add(scrollUtil, BorderLayout.CENTER);

        // Gestion du panneau de discussion
        JPanel panelDisc = new JPanel(new BorderLayout(5, 5));
        panelDisc.add(new JLabel("Discussion"), BorderLayout.NORTH);
        panelDisc.add(scrollDis, BorderLayout.CENTER);

        // Ajout et positionnement des elements au panel
        JPanel panel = new JPanel(new BorderLayout(10, 10));
        panel.setBorder(new EmptyBorder(10,10,10,10));
        panel.add(statut, BorderLayout.NORTH);
        panel.add(panelUtil,BorderLayout.CENTER);
        panel.add(panelDisc, BorderLayout.PAGE_END);


        add(panel); 
    }


    // ********************* //
    // ****** GETTERS ****** //
    // ********************* //


    /**
     * Getter de la discussion
     * @return la zone ou il y a la discussion
     */
    public JTextArea getDiscussion() {
        return discussion;
    }

    // ********************* //
    // ****** SETTERS ****** //
    // ********************* //    
    
    
    
    /**
     * Méthode permettant de regler le statut du serveur
     * @param msg le statut
     */
    public void setStatut(String msg) {
        this.statut.setText(msg);
    }



    

    /**
     * Méthode permettant de supprimer la liste des users
     */
    public void effacerUtilisateursFenetre() {
        users.setText(""); //effacer tout le contenu
    }

    /**
     * Méthode permettant d'ajouter un utilisateur dans la liste des personnes connectées
     * @param nom nom a ajouter a la liste
     */
    public void ajouterUtilisateurFenetre(String nom) {
        users.append(nom+"\n");
    }







    // ******************* //
    // PROGRAMME PRINCIPAL //
    // ******************* //


    /**
     * Programme princiapl permettant d'ouvrir une fenetre cote Serveur
     * @param args arguments de la ligne de commande
     */
    public static void main(String[] args) {
        new Serveur(Serveur.port).lancer();
    }
}
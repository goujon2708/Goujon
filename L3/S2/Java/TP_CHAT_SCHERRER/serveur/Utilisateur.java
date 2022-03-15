/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */


package serveur;
import java.awt.Color;

import java.util.Random;

/**
 * La classe Utilisateur permet d'associer à chaque utilisateur une color
 * 
 *  Les VI de la classe sont :::
 *      
 *         - name       ==> name de l'utilisateur
 *         - color      ==> couleur associée à l'utilisateur
 *         - connecte   ==> boolean permettant de connaître le statut de l'utilisateur
 */
public class Utilisateur {

    private String name;
    private Color color;
    private boolean connecte;

    /**
     * Constructeur permettant de creer un utilisateur
     * @param name name de l'utilisateur
     */
    public Utilisateur(String name) {
        this.name = name;
        this.connecte = true;
        this.color = null;
    }

    /**
     * Méthode permettant de generer une color
     * @return la color generee
     */
    public Color genererCouleur() {
        Random rand = new Random();
        int r = rand.nextInt(255);
        int g = rand.nextInt(255);
        int b = rand.nextInt(255);

        return (new Color(r,g,b));
    }



    // ********************** //
    // ****** GETTERS ******* //
    // ********************** //


    /**
     * Acces en lecture du nom de l'utilisateur
     * @return le name
     */
    public String getNom() {
        return name;
    }

    /**
     * Acces en lecture  de la color de l'utilisateur
     * @return la color
     */
    public int getCouleur() {
        return color.getRGB();
    }

    /**
     * Acces en lecture de la connexion ou non de l;utilisateur
     * @return un booleen
     */
    public boolean getConnecte() {
        return connecte;
    }





    // ********************** //
    // ****** SETTERS ******* //
    // ********************** //


    /**
     * Méthode permettant de modifier le statut de l'utilisateur
     * @param connecte valeur du statut
     */
    public void setConnecte(boolean connecte) {
        this.connecte = connecte;
    }

    /**
     * Méthode permettant d'attribuer une color à un utilisateur
     * @param color color a assigner a l'utilisateur
     */
    public void setCouleur(Color color) {
        this.color = color;
    }
}

package client;

import java.awt.FlowLayout;

import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;


/**
 * La classe SaisieConnexion va gérer le placement du label et la zone de texte lorsque le client veut se connecter
 * 
 *  Les VI de la classe sont :::
 * 
 *      - label             ==> label pour la zone de saisie
 *      - saisie            ==> zone réservée à la saisie
 */
public class SaisieConnexion extends JPanel {

    private JLabel label;
    private JTextField saisie;

    /**
     * Constructeur de la classe SaisieConnexion
     * @param nomLabel nom du label
     */
    public SaisieConnexion(String nomLabel) {
        this.label = new JLabel(nomLabel);
        this.saisie = new JTextField(15);

        this.setLayout(new FlowLayout(FlowLayout.TRAILING, 15, 5));

        this.add(label);
        this.add(saisie);
    }

    // **************************************************** //
    // ****** GETTERS DE LA CLASSE PANNEAUCONNEXION ******* //
    // **************************************************** //
    /**
     * Getter de la saisie du client
     * @return la saisie du client
     */
    public String getSaisie() {
        return saisie.getText();
    }

    /**
     * Getter du JTextField
     * @return le JTextField
     */
    public JTextField getTextField() {
        return saisie;
    }
}

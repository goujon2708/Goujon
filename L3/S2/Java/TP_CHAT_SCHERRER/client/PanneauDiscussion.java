/**
 * TP - Chat - L3 INFO
 * 
 * @author : Scherrer Arthur
 */

package client;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.io.BufferedReader;
import java.io.FileReader;

import java.util.Map;

import java.util.concurrent.ConcurrentHashMap;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextPane;

import javax.swing.border.EmptyBorder;

import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;

import javax.swing.text.AttributeSet;
import javax.swing.text.BadLocationException;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;
import javax.swing.text.StyledDocument;


/**
 * La classe PanneauDiscussion hérite de JPanel. Elle représente la partie "discussion" de la fenêtre du client
 * 
 *  Les VI de la classe PanneauDiscussion sont :::
 * 
 *      - connectes         ==> zone réservée pour afficher les personnes connectées
 *      - discussion        ==> zone qui affichera la discussion
 *      - saisieMessage     ==> zone pour écrire un message
 *      - button            ==> boutton pour envoyer un message
 *      - choixMessage      ==> comboBox pour choisir le destinataire
 *      - fenêtre           ==> fenêtre du client
 *      - optionEnvoie      ==> option d'envoi
 *      - colors          ==> Stockage des noms des personnes connectées et leurs colors associées
 */
public class PanneauDiscussion extends JPanel {

    private JTextPane connectes;
    private JTextPane discussion;
    private JTextArea saisieMessage;
    private JButton button;
    private JComboBox<String> choixMessage;
    private String optionEnvoi;
    private FenetreClient fenetre;
    private ConcurrentHashMap<String, Color> colors;

    /**
     * Constructeur de la PanneauDiscussion
     *
     * @param f fenetre du client
     */
    public PanneauDiscussion(FenetreClient f) {
        
        this.colors = new ConcurrentHashMap<>();
        this.connectes = new JTextPane();
        this.discussion = new JTextPane();
        this.saisieMessage = new JTextArea(5, 28);
        this.button = new JButton("Envoyer");
        this.fenetre = f;
        this.choixMessage = new JComboBox<>();
        this.optionEnvoi = "Tout le monde";

        // Ajout de barres de scrolling pour la liste des personnes connectées et la discussion
        JScrollPane scrollConn = new JScrollPane(connectes);
        scrollConn.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED);
        JScrollPane scrollDisc = new JScrollPane(discussion);
        scrollDisc.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        scrollDisc.setPreferredSize(new Dimension(320, 350));

        // Les zones ont sont inscrits les participants à la discussion ne doivent pas être éditables
        this.connectes.setEditable(false);
        this.discussion.setEditable(false);

        
        this.connectes.setPreferredSize(new Dimension(130, 80));
        this.connectes.setCaretPosition(connectes.getDocument().getLength());

        this.saisieMessage.getDocument().addDocumentListener(new TextAreaListener());

        this.button.setEnabled(false);

        this.button.addActionListener(new ActionListener() {
            /**
             * Méthode qui est appelée quand le client va cliquer sur le bouton 'Envoyer'
             * @param e evenement
             */
            @Override
            public void actionPerformed(ActionEvent e) {
                fenetre.getClient().envoyerMessage(getMessage(), optionEnvoi); 
                saisieMessage.setText(""); // On supprime le texte de la saisie message
            }
        });

        JPanel panelConnectes = new JPanel(new BorderLayout(10, 10));
        JPanel panelDiscussion = new JPanel(new BorderLayout(10, 10));
        JPanel panelChoixMessage = new JPanel();
        JPanel panelMessage = new JPanel(new BorderLayout(10, 10));
        JPanel panelDroit = new JPanel(new BorderLayout(10, 10));

        // Gestion de la partie gauche
        panelConnectes.add(new JLabel("Connectes"), BorderLayout.NORTH);
        panelConnectes.add(scrollConn, BorderLayout.CENTER);

        // Gestion du panel avec la combobox
        panelChoixMessage.add(new JLabel("Message a "));
        choixMessage.setPreferredSize(new Dimension(250,25));
        panelChoixMessage.add(choixMessage);

        // Ajout d'un listener sur la combobox
        choixMessage.addActionListener(new ActionListener() {
            /**
             * Méthode qui est appelee quand met a jour l'option d'envoi choisi par le
             * client, chaque fois qu'il interagit avec la combobox
             * @param e evenement
             */
            @Override
            public void actionPerformed(ActionEvent e) {
                optionEnvoi = choixMessage.getItemAt(choixMessage.getSelectedIndex());
            }
        });

        // Gestion de la partie droite
        panelDiscussion.add(new JLabel("Discussion"), BorderLayout.NORTH);
        panelDiscussion.add(scrollDisc, BorderLayout.SOUTH);

        panelMessage.add(panelChoixMessage, BorderLayout.NORTH);
        panelMessage.add(saisieMessage, BorderLayout.SOUTH);

        panelDroit.add(panelDiscussion, BorderLayout.NORTH);
        panelDroit.add(panelMessage, BorderLayout.CENTER);
        panelDroit.add(button, BorderLayout.PAGE_END);

        // Accrochages des panels au PanneauDiscussion
        this.setLayout(new BorderLayout(25, 25));
        this.setBorder(new EmptyBorder(10, 10, 10, 10));
        this.add(panelDroit, BorderLayout.EAST);
        this.add(panelConnectes, BorderLayout.WEST);

        this.setPreferredSize(new Dimension(300, 450));
    }




    // ***************************************************** //
    // ****** GETTERS DE LA CLASSE PANNEAUDISCUSSION ******* //
    // ***************************************************** //
    /**
     * Getter du message saisi par l'utilisateur
     * @return le message
     */
    public String getMessage() {
        return saisieMessage.getText();
    }

    /**
     * Getter de la discussion
     * @return la discussion
     */
    public JTextPane getDiscussion() {
        return discussion;
    }

    /**
     * Getter de du tableau des noms d'utilisateurs et de leurs colors
     * @return le tableau des noms d'utilisateurs associes a leur couleur
     */
    public ConcurrentHashMap<String, Color> getCouleurs() {
        return colors;
    }






    /**
     * Méthode permettant d'effacer la discussion (utilise lors de la deconnexion)
     */
    public void effacerDiscussion() {
        discussion.setText("");
    }

    /**
     * Méthode permettant de vider la liste des personnes connectes
     */
    public void effacerConnectes() {
        connectes.setText("");
    }

    /**
     * Méthode permettant de mettre a jour l'affichage des personnes connectees =>
     */
    public void majAffichageConnectes() {
        effacerConnectes(); 

        choixMessage.removeAllItems(); 
        choixMessage.addItem("Tout le monde");
        choixMessage.setSelectedIndex(0); // Par defaut, envoi a tout le monde

        // Parcours de la liste des personnes connectees
        for (Map.Entry<String, Color> entry : colors.entrySet()) {
            String nom = entry.getKey(); 
            Color rgb = new Color(chercherCouleur(nom));

            if(!fenetre.getClient().getNom().equals(nom)) {
                choixMessage.addItem(nom);
            }

            // Mise a jour de l'affichage dans le panneau "Connectes"
            StyledDocument doc = connectes.getStyledDocument();
            StyleContext style = StyleContext.getDefaultStyleContext();
            
            AttributeSet aset = style.addAttribute(style.getEmptySet(), StyleConstants.Foreground, rgb); // Modification de la couleur
            aset = style.addAttributes(aset, style.addAttribute(style.getEmptySet(), StyleConstants.Bold, true));

            // ajout de la personne dans la liste avec la couleur correspondante
            try {
                doc.insertString(doc.getLength(), nom+"\n", aset);
            } catch(BadLocationException e) {
                e.printStackTrace();
            }
        }

        System.out.println("maj de l'affichage de la liste des connectes");
    }

    /**
     * Méthode permettant de trouver la couleur d'un client donné
     * @param nom nom du client pour qui on cherche sa couleur
     * @return la couleur (sous forme rgb = un entier)
     */
    public int chercherCouleur(String nom) {
        // Lecture dans le fichier "utilisateurs.txt"
        try (BufferedReader reader = new BufferedReader(new FileReader("utilisateurs.txt"))) {
            String line = "";

            while ((line = reader.readLine()) != null) {
                String[] tmp = (line.split(":")); 

                String s = tmp[0];
                if(s.equalsIgnoreCase(nom)) {
                    return Integer.valueOf(tmp[1]);
                }
            }

        } catch(Exception ex) {
            ex.printStackTrace();
            System.out.println(ex.getMessage());
        }
        return 0; // si on n'a pas trouvé le nom dans la liste
    }

    /**
     * Méthode permettant d'ajouter un client dans la liste des personnes connectées
     * @param nom nom du client à ajouter
     */
    public void ajouterClientListe(String nom) {
        if(!colors.containsKey(nom)) {
            Color couleur = new Color(chercherCouleur(nom));
            colors.put(nom, couleur);
        }
    }

    /**
     * Méthode qui permer de vider la liste des connectes
     */
    public void videListeClient() {
        colors.clear();
    }

    /**
     * Classe interne pour gerer le listener de la saisie du message
     */
    private class TextAreaListener implements DocumentListener{
        /**
         * Méthode permettant de savoir si quelque chose a ete ajoute au document
         * @param e evenement
         */
        @Override
        public void insertUpdate(DocumentEvent e) {
            verifierSaisie();
        }

        /**
         * Méthode permettant de savoir si quelque chose a ete supprime du document
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
         * Méthode permettant de verifier si le client a saisi quelque chose dans la zone de texte
         */
        public void verifierSaisie() {
            boolean ok = true;

            // On regarde si le client a ecrit quelque chose
            if(saisieMessage.getText().trim().equals(""))
                ok = false;

            if(ok)
                button.setEnabled(true); 
            else
                button.setEnabled(false); 
        }
    }

    
}
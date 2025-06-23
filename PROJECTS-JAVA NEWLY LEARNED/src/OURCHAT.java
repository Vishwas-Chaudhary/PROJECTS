import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class OURCHAT extends JFrame {

    private JTextArea chatAreaLeft, chatAreaRight;
    private JTextArea messageAreaLeft, messageAreaRight;
    private JButton sendButtonLeft, sendButtonRight;

    public OURCHAT() {
        setTitle("OURCHAT - Two-Way Colorful Chat Messenger");
        setSize(900, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        setLayout(new BorderLayout());

        // Left chat panel (User 1)
        JPanel leftPanel = new JPanel(new BorderLayout(5, 5));
        leftPanel.setBorder(BorderFactory.createTitledBorder("User 1"));
        chatAreaLeft = createChatArea(new Color(240, 255, 255));
        messageAreaLeft = createMessageArea();
        sendButtonLeft = createSendButton(new Color(70, 130, 180));

        JScrollPane scrollPaneLeft = new JScrollPane(chatAreaLeft);
        JScrollPane messageScrollLeft = new JScrollPane(messageAreaLeft);

        JPanel inputPanelLeft = new JPanel(new BorderLayout(5, 5));
        inputPanelLeft.add(messageScrollLeft, BorderLayout.CENTER);
        inputPanelLeft.add(sendButtonLeft, BorderLayout.EAST);

        leftPanel.add(scrollPaneLeft, BorderLayout.CENTER);
        leftPanel.add(inputPanelLeft, BorderLayout.SOUTH);

        // Right chat panel (User 2)
        JPanel rightPanel = new JPanel(new BorderLayout(5, 5));
        rightPanel.setBorder(BorderFactory.createTitledBorder("User 2"));
        chatAreaRight = createChatArea(new Color(255, 240, 245));
        messageAreaRight = createMessageArea();
        sendButtonRight = createSendButton(new Color(255, 105, 180));

        JScrollPane scrollPaneRight = new JScrollPane(chatAreaRight);
        JScrollPane messageScrollRight = new JScrollPane(messageAreaRight);

        JPanel inputPanelRight = new JPanel(new BorderLayout(5, 5));
        inputPanelRight.add(messageScrollRight, BorderLayout.CENTER);
        inputPanelRight.add(sendButtonRight, BorderLayout.EAST);

        rightPanel.add(scrollPaneRight, BorderLayout.CENTER);
        rightPanel.add(inputPanelRight, BorderLayout.SOUTH);

        // Split pane
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, leftPanel, rightPanel);
        splitPane.setDividerLocation(450);
        add(splitPane, BorderLayout.CENTER);

        addShapesBackground();

        // Send actions
        sendButtonLeft.addActionListener(e -> sendMessage(messageAreaLeft, chatAreaLeft, chatAreaRight, "User 1"));
        sendButtonRight.addActionListener(e -> sendMessage(messageAreaRight, chatAreaRight, chatAreaLeft, "User 2"));

        // Enter key shortcuts
        messageAreaLeft.addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER && !e.isShiftDown()) {
                    e.consume();
                    sendButtonLeft.doClick();
                }
            }
        });

        messageAreaRight.addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER && !e.isShiftDown()) {
                    e.consume();
                    sendButtonRight.doClick();
                }
            }
        });
    }

    private JTextArea createChatArea(Color bgColor) {
        JTextArea ta = new JTextArea();
        ta.setEditable(false);
        ta.setLineWrap(true);
        ta.setWrapStyleWord(true);
        ta.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        ta.setBackground(bgColor);
        ta.setBorder(BorderFactory.createLineBorder(Color.GRAY, 2));
        return ta;
    }

    private JTextArea createMessageArea() {
        JTextArea ta = new JTextArea(3, 20);
        ta.setLineWrap(true);
        ta.setWrapStyleWord(true);
        ta.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        ta.setBorder(BorderFactory.createLineBorder(Color.GRAY, 1));
        return ta;
    }

    private JButton createSendButton(Color bgColor) {
        JButton btn = new JButton("Send");
        btn.setBackground(bgColor);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setFont(new Font("Segoe UI", Font.BOLD, 14));
        return btn;
    }

    private void sendMessage(JTextArea inputArea, JTextArea senderChat, JTextArea receiverChat, String user) {
        String message = inputArea.getText().trim();
        if (!message.isEmpty()) {
            String formattedMessage = user + ": " + message + "\n";
            senderChat.append(formattedMessage);
            receiverChat.append(formattedMessage);
            inputArea.setText("");
            senderChat.setCaretPosition(senderChat.getDocument().getLength());
            receiverChat.setCaretPosition(receiverChat.getDocument().getLength());
        }
    }

    private void addShapesBackground() {
        JComponent glass = new JComponent() {
            @Override
            protected void paintComponent(Graphics g) {
                Graphics2D g2d = (Graphics2D) g;
                int w = getWidth();
                int h = getHeight();

                GradientPaint gp = new GradientPaint(0, 0, new Color(255, 192, 203, 80),
                        w, h, new Color(135, 206, 250, 80));
                g2d.setPaint(gp);
                g2d.fillRect(0, 0, w, h);

                g2d.setColor(new Color(255, 105, 180, 60));
                for (int i = 0; i < 6; i++) {
                    int size = 120 + i * 30;
                    g2d.fillOval(50 * i, 30 * i, size, size);
                }

                g2d.setColor(new Color(30, 144, 255, 60));
                for (int i = 0; i < 6; i++) {
                    g2d.fillRect(70 * i, 50 * i, 60, 30);
                }
            }
        };
        getLayeredPane().add(glass, JLayeredPane.PALETTE_LAYER);
        glass.setBounds(0, 0, getWidth(), getHeight());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            OURCHAT chat = new OURCHAT();
            chat.setVisible(true);
        });
    }
}

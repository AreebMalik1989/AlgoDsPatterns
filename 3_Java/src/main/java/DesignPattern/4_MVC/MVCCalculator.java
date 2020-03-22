import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import javax.swing.*;

public class MVCCalculator {
    
    public static void main(final String[] args) {

        final CalculatorView theView = new CalculatorView();
        final CalculatorModel theModel = new CalculatorModel();
        final CalculatorController theController = new CalculatorController(theView, theModel);

        theView.setVisible(true);
    }
}

/**
 * This is the View. Its only job is to display what the user sees. It performs
 * no calculations, but instead passes information entered by the user to
 * whomever needs it.
 */
class CalculatorView extends JFrame {

    /**
     * Default generated serialVersionUID
     */
    private static final long serialVersionUID = 1L;

    private final JTextField firstNumber = new JTextField(10);
    private final JLabel additionLabel = new JLabel("+");
    private final JTextField secondNumber = new JTextField(10);
    private final JButton calculateButton = new JButton("Calculate");
    private final JTextField calcSolution = new JTextField(10);

    public CalculatorView() {

        // Sets up the view and adds the components

        final JPanel calcPanel = new JPanel();

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(600, 200);

        calcPanel.add(firstNumber);
        calcPanel.add(additionLabel);
        calcPanel.add(secondNumber);
        calcPanel.add(calculateButton);
        calcPanel.add(calcSolution);

        this.add(calcPanel);

        // End of setting up the components --------
    }

    public int getFirstNumber() {
        return Integer.parseInt(firstNumber.getText());
    }

    public int getSecondNumber() {
        return Integer.parseInt(secondNumber.getText());
    }

    public int getCalcSolution() {
        return Integer.parseInt(calcSolution.getText());
    }

    public void setCalcSolution(final int solution) {
        calcSolution.setText(Integer.toString(solution));
    }

    // If the calculateButton is clicked execute a method
    // in the Controller named actionPerformed
    void addCalculateListener(final ActionListener listenForCalcButton) {
        calculateButton.addActionListener(listenForCalcButton);
    }

    // Open a popup that contains the error message passed
    void displayErrorMessage(final String errorMessage) {
        JOptionPane.showMessageDialog(this, errorMessage);
    }
}

/**
 * The Model class performs all the calculations needed and that is it. It
 * doesn't know the View exists
 */
class CalculatorModel {

    // Holds the value of the sum of the numbers
    // entered in the view
    private int calculationValue;

    public void addTwoNumbers(final int firstNumber, final int secondNumber) {
        calculationValue = firstNumber + secondNumber;
    }

    public int getCalculationValue() {
        return calculationValue;
    }
}

/**
 * The Controller coordinates interacations between the view and the model
 */
class CalculatorController implements ActionListener {

    private final CalculatorView theView;
    private final CalculatorModel theModel;

    public CalculatorController(final CalculatorView theView, final CalculatorModel theModel) {
        this.theView = theView;
        this.theModel = theModel;

        // Tell the View that when ever the calculate button
        // is clicked to execute the actionPerformed method
        // in the CalculateListener inner class
        this.theView.addCalculateListener(this);
    }

    @Override
    public void actionPerformed(final ActionEvent e) {

        int firstNumber = 0, secondNumber = 0;

        // Surround interactions with the view with
        // a try block in case numbers weren't
        // properly entered
        try {
            firstNumber = theView.getFirstNumber();
            secondNumber = theView.getSecondNumber();

            theModel.addTwoNumbers(firstNumber, secondNumber);
            theView.setCalcSolution(theModel.getCalculationValue());
        }

        catch (final NumberFormatException ex) {
            System.out.println(ex);
            theView.displayErrorMessage("You Need to Enter 2 Integers");
        }
    }
}
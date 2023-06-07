package com.murach.tipcalculator;

import java.text.NumberFormat;

import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;
import android.app.Activity;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;

public class TipCalculatorActivity extends Activity 
implements OnEditorActionListener, OnClickListener {

    // define variables for the widgets
    private EditText billAmountEditText;
    private TextView percentTextView;   
    private Button   percentUpButton;
    private Button   percentDownButton;
    private TextView tipTextView;
    private TextView totalTextView;
    private RadioGroup roundingRadioGroup;
    private RadioButton roundNoneRadioButton;
    private RadioButton roundTipRadioButton;
    private RadioButton roundTotalRadioButton;
    private Spinner splitSpinner;
    
    // define the SharedPreferences object
    private SharedPreferences savedValues;

    // define rounding constants
    private final int ROUND_NONE = 0;
    private final int ROUND_TIP = 1;
    private final int ROUND_TOTAL = 2;
    
    // define instance variables that should be saved
    private String billAmountString = "";
    private float tipPercent = .15f;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tip_calculator);
        
        // get references to the widgets
        billAmountEditText = (EditText) findViewById(R.id.billAmountEditText);
        percentTextView = (TextView) findViewById(R.id.percentTextView);
        percentUpButton = (Button) findViewById(R.id.percentUpButton);
        percentDownButton = (Button) findViewById(R.id.percentDownButton);
        tipTextView = (TextView) findViewById(R.id.tipTextView);
        totalTextView = (TextView) findViewById(R.id.totalTextView);
        roundingRadioGroup = (RadioGroup)
                findViewById(R.id.roundingRadioGroup);
        roundNoneRadioButton = (RadioButton)
                findViewById(R.id.roundNoneRadioButton);
        roundTipRadioButton = (RadioButton)
                findViewById(R.id.roundTipRadioButton);
        roundTotalRadioButton = (RadioButton)
                findViewById(R.id.roundTotalRadioButton);

        // set the listeners
        billAmountEditText.setOnEditorActionListener(this);
        percentUpButton.setOnClickListener(this);
        percentDownButton.setOnClickListener(this);
        roundingRadioGroup.setOnCheckedChangeListener(this);
        roundingRadioGroup.setOnKeyListener(this);
        
        // get SharedPreferences object
        savedValues = getSharedPreferences("SavedValues", MODE_PRIVATE);        
    }
    
    @Override
    public void onPause() {
        // save the instance variables       
        Editor editor = savedValues.edit();        
        editor.putString("billAmountString", billAmountString);
        editor.putFloat("tipPercent", tipPercent);
        editor.putInt("rounding", rounding);
        editor.commit();        

        super.onPause();      
    }
    
    @Override
    public void onResume() {
        super.onResume();
        
        // get the instance variables
        billAmountString = savedValues.getString("billAmountString", "");
        tipPercent = savedValues.getFloat("tipPercent", 0.15f);
        rounding = savedValues.getInt("rounding", ROUND_NONE);
        // set the bill amount on its widget
        billAmountEditText.setText(billAmountString);

        // set the tip percent on its widget
        int progress = Math.round(tipPercent * 100);
        percentSeekBar.setProgress(progress);

        // set rounding on radio buttons
        // NOTE: this executes the onCheckedChanged method,
        // which executes the calculateAndDisplay method
        if (rounding == ROUND_NONE) {
            roundNoneRadioButton.setChecked(true);
        }
        else if (rounding == ROUND_TIP) {
            roundTipRadioButton.setChecked(true);
        }
        else if (rounding == ROUND_TIP) {
            roundTotalRadioButton.setChecked(true);
        }

        // calculate and display
        calculateAndDisplay();
    }    
    
    public void calculateAndDisplay() {        

        // get the bill amount
        billAmountString = billAmountEditText.getText().toString();
        float billAmount; 
        if (billAmountString.equals("")) {
            billAmount = 0;
        }
        else {
            billAmount = Float.parseFloat(billAmountString);
            // calculate tip and total
            float tipAmount = 0;
            float totalAmount = 0;
            if (rounding == ROUND_NONE) {
                tipAmount = billAmount * tipPercent;
                totalAmount = billAmount + tipAmount;
            }
            else if (rounding == ROUND_TIP) {
                tipAmount = StrictMath.round(billAmount * tipPercent);
                totalAmount = billAmount + tipAmount;
            }
            else if (rounding == ROUND_TOTAL) {
                float tipNotRounded = billAmount * tipPercent;
                totalAmount = StrictMath.round(billAmount + tipNotRounded);
                tipAmount = totalAmount - billAmount;
            }

        
        // display the other results with formatting
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        tipTextView.setText(currency.format(tipAmount));
        totalTextView.setText(currency.format(totalAmount));
        
        NumberFormat percent = NumberFormat.getPercentInstance();
        percentTextView.setText(percent.format(tipPercent));
    }
    
    @Override
    public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
        if (actionId == EditorInfo.IME_ACTION_DONE ||
    		actionId == EditorInfo.IME_ACTION_UNSPECIFIED) {
            calculateAndDisplay();
        }        
        return false;
    }

        @Override
        public void onCheckedChanged(RadioGroup group, int checkedId) {
            switch (checkedId) {
                case R.id.roundNoneRadioButton:
                    rounding = ROUND_NONE;
                    break;
                case R.id.roundTipRadioButton:
                    rounding = ROUND_TIP;
                    break;
                case R.id.roundTotalRadioButton:
                    rounding = ROUND_TOTAL;
                    break;
            }
            calculateAndDisplay();
        }


        @Override
    public void onClick(View v) {
        switch (v.getId()) {
        case R.id.percentDownButton:
            tipPercent = tipPercent - .01f;
            calculateAndDisplay();
            break;
        case R.id.percentUpButton:
            tipPercent = tipPercent + .01f;
            calculateAndDisplay();
            break;
        }
    }
}
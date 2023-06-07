package com.murach.invoice;

import java.text.NumberFormat;

import android.os.Bundle;
import android.app.Activity;
import android.view.KeyEvent;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;  //imports listener
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;

public class InvoiceTotalActivity extends Activity
implements OnEditorActionListener {                    //implements listeners

	//Declare variables for the widgets
	private EditText subtotalEditText;
	private TextView discountPercentTextView;
	private TextView discountAmountTextView;
	private TextView totalTextView;

	//define sharedPreferences object
	private SharedPreferences savedValues;

	//defining instance variable for discount percent
	private String subtotalString = "";


	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_invoice_total);

		//Get references to the widgets
		subtotalEditText = (EditText) findViewById(R.id.subtotalEditText);
		discountPercentTextView = (TextView) findViewById(R.id.discountPercentTextView);
		discountAmountTextView = (TextView) findViewById(R.id.discountAmountTextView);
		totalTextView = (TextView) findViewById(R.id.totalTextView);

		//sets listener
		subtotalEditText.setOnEditorActionListener(this);

		//get sharedPrefrences object
		savedValues = getSharedPreferences("SavedValues", MODE_PRIVATE);
	}

	//save the instance variables
	@Override
	public void onPause() {
		Editor editor = savedValues.edit();
		editor.putString("subtotalString", subtotalString);
		editor.apply();

		super.onPause();
	}

	@Override
	public void onResume() {
		super.onResume();

		//get the instance variables
		subtotalString = savedValues.getString("subtotalString", "");

		//setting the invoice amount
		subtotalEditText.setText(subtotalString);

		//calculate and display
		calculateAndDisplay();
	}

	//get bill amount
	public void calculateAndDisplay() {

		//get bill amount
		subtotalString = subtotalEditText.getText().toString();
		float subtotal;
		if (subtotalString.equals("")) {
			subtotal = 0;
		} else {
			subtotal = Float.parseFloat(subtotalString);
		}

		//calculate tip and total
		float discountPercent;
		if (subtotal >= 200) {
			discountPercent = .2f;
		}
		else if (subtotal >= 100) {
			discountPercent = .1f;
		}
		else {
			discountPercent = 0;
		}
		//calculating discount
		float discountAmount = subtotal * discountPercent;
		float total = subtotal - discountAmount;

		NumberFormat percent = NumberFormat.getPercentInstance();
		discountPercentTextView.setText(percent.format(discountPercent));

		//display the results with formatiing
		NumberFormat currency = NumberFormat.getCurrencyInstance();

		discountAmountTextView.setText(currency.format(discountAmount));
		totalTextView.setText(currency.format(total));
	}

	//implements the listener
	@Override
	public boolean onEditorAction(TextView v, int actionID, KeyEvent event) {
		calculateAndDisplay();

		return false;

	}
}
package com.murach.tipcalculator;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.util.Log;

public class ConnectivityReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d("Calculator App", "Connection change");

        //network check
        ConnectivityManager connectivityManager = (ConnectivityManager)
                context.getSystemService(Context.CONNECTIVITY_SERVICE);

        NetworkInfo networkInfo = connectivityManager.getActiveNetworkInfo();

        Intent service = new Intent(context, TipCalculatorActivity.class);

        if (networkInfo != null && networkInfo.isConnected()) {
            Log.d("Calculator App", "Connected");
            context.startService(service);
        }
        else {
            Log.d("Calculator App", "NOT connected");
            context.stopService(service);
        }
    }
}

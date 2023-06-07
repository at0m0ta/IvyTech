package com.murach.tipcalculator;

import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.util.Log;

public class BootReceiver extends BroadcastReceiver {

    //Logcat boot sequence broadcast
    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d("Calculator App", "Boot completed!");

        //START ON BOOT
        if (Intent.ACTION_BOOT_COMPLETED.equals(intent.getAction())) {
            Intent ActivityIntent = new Intent(context, TipCalculatorActivity.class);
            ActivityIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            context.startActivities(new Intent[]{ActivityIntent});
        }
    }


}

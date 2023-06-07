package com.murach.reminder;

import java.util.Timer;
import java.util.TimerTask;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

import java.util.Timer;

public class ReminderService extends Service {

    private ReminderApp app;
    private Timer timer;
    private FileIO io;

    @Override
    public void onCreate() {
        Log.d("Reminder App" "Service Started");
        app = (ReminderApp) getApplication();

    }

    @Override int onStop() {

    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }
    private void startTimer() {

    }
}

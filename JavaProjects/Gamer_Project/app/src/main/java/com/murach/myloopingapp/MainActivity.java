package com.murach.myloopingapp;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //Use fullscreen capability
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN );
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);

        //GameView class created earlier
        setContentView(new GameView(this));
    }
}

package com.murach.tweenanimation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    ImageView iv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        iv = (ImageView)findViewById(R.id.skateImg);
    }

    public void onMove(View v) {
        Animation animation = AnimationUtils.loadAnimation(getApplicationContext(), R.anim.anim);
        iv.startAnimation(animation);
    }
}

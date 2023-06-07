package com.murach.myimagesound;

import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Audio sounds
        final MediaPlayer crunch_sound_mp = MediaPlayer.create(this, R.raw.bite);

        final Button play_crunchy = (Button) this.findViewById(R.id.crunch_apple);

        play_crunchy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                crunch_sound_mp.start();
            }
        });


        //Display Image
        ImageView my_image = (ImageView) findViewById(R.id.my_image);
        my_image.setImageResource(R.drawable.android_background);

    }
}

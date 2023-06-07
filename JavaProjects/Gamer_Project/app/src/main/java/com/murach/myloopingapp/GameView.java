package com.murach.myloopingapp;

import android.content.Context;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.view.SurfaceView;
import android.view.SurfaceHolder;

//the following will be our canvas, which will show our graphics on
//the touch screen; the canvas, "GameView", will be updated by a thread
//
public class GameView extends SurfaceView implements SurfaceHolder.Callback {

    private MainThread thread;
    private CharacterSprite characterSprite;

    public  GameView(Context context) {
        //calling surfaceview superclass
        super(context);

        //intercept events
        getHolder().addCallback(this);

        //building a new thread
        thread = new MainThread(getHolder(), this);
        setFocusable(true);
    }

    //overriding methods
    @Override
    public  void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {

    }

    @Override
    public void surfaceCreated(SurfaceHolder holder) {
        characterSprite = new CharacterSprite(BitmapFactory.decodeResource(getResources(), R.drawable.avdgreen));

        //start thread
        thread.setRunning(true);
        thread.start();
    }

    @Override
    public void surfaceDestroyed(SurfaceHolder holder) {
        //stop the thread
        boolean retry = true;
        while (retry) {
            try {
                thread.setRunning(false);
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            retry = false;
        }
    }

public void update() {
      characterSprite.update();

}
@Override
    public  void draw(Canvas canvas) {
        super.draw(canvas);
        if (canvas!=null) {
        characterSprite.draw(canvas);
        }

}

}

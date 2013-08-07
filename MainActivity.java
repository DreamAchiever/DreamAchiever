package com.example.create;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.MotionEvent;
import android.view.View;
import android.view.View.OnTouchListener;
import android.widget.FrameLayout;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        FrameLayout fl=(FrameLayout)findViewById(R.id.mylayout);
        final RabbitView rabbit=new RabbitView(MainActivity.this);
        rabbit.setOnTouchListener(new OnTouchListener(){
        	public boolean onTouch(View v,MotionEvent event)
        	{
        		rabbit.bitmapX=event.getX();
        		rabbit.bitmapY=event.getY();
        		rabbit.invalidate();
        		return true;
        	}
        });
        fl.addView(rabbit);
    }


   /* @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }*/
    
}

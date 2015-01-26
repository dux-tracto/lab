package org.takle.roku;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.LinkedHashMap;
import java.util.Map;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends Activity {
	public static final String HTTP = "http://";
	public static final String KEYPRESS = "/keypress/";
	public static final String ROKU_PORT = "192.168.0.37:8060";
	public static final String KEY_HOME = "Home";
	public static final String PRESS_MESSAGE = "org.takle.roku.BUTTON_PRESSED";
	public enum Button {BACK, HOME, UP}
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}

	public void go(View view, Button button) {
		Intent intent;
		EditText editText;
		String message;

		switch (button) {
		case BACK:
			message = "back";
			break;
			
		case HOME:
			message = "home";
			break;
			
		case UP:
			message = "up";
			break;
			
        default:
			message = "unknown";
			break;
		}

		intent = new Intent(this, DisplayPressAckActivity.class);
		intent.putExtra(PRESS_MESSAGE, message);
		startActivity(intent);
	}

	public void goBack(View view) {
		Log.i(getPackageName(), "Back pressed");
		new ButtonPusher().execute("Back");
	}


	public void goInfo(View view) {
		Log.i(getPackageName(), "Info pressed");
		new ButtonPusher().execute("Info");
	}

	public void goHome(View view) {
		Log.i(getPackageName(), "Home pressed");
		new ButtonPusher().execute("Home");
	}

	public void goUp(View view) {
		Log.i(getPackageName(), "up pressed");
		new ButtonPusher().execute("Up");
	}

	public void goDown(View view) {
		Log.i(getPackageName(), "Down pressed");
		new ButtonPusher().execute("Down");
	}

	public void goLeft(View view) {
		Log.i(getPackageName(), "Left pressed");
		new ButtonPusher().execute("Left");
	}

	public void goRight(View view) {
		Log.i(getPackageName(), "Right pressed");
		new ButtonPusher().execute("Right");
	}

	public void goSelect(View view) {
		Log.i(getPackageName(), "Select pressed");
		new ButtonPusher().execute("Select");
	}

	public void goReverse(View view) {
		Log.i(getPackageName(), "Reverse pressed");
		new ButtonPusher().execute("Rev");
	}

	public void goPlay(View view) {
		Log.i(getPackageName(), "Play pressed");
		new ButtonPusher().execute("Play");
	}

	public void goForward(View view) {
		Log.i(getPackageName(), "Forward pressed");
		new ButtonPusher().execute("Fwd");
	}

	private class ButtonPusher extends AsyncTask<String, String, String> {

		@Override
		protected String doInBackground(String... params) {
			StringBuilder urlString = new StringBuilder();
			String nothing = "";
			URL url = null;
			Reader in = null;
			byte[] postDataBytes = null;
			HttpURLConnection conn = null;
			int c;
			
			try {
				urlString.append(HTTP);
				urlString.append(ROKU_PORT);
				urlString.append(KEYPRESS);
				urlString.append(params[0]);
				url = new URL(urlString.toString());
				postDataBytes = nothing.toString().getBytes("UTF-8");

				conn = (HttpURLConnection) url.openConnection();
				conn.setRequestMethod("POST");
				conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
				conn.setRequestProperty("Content-Length", Integer.toString(nothing.length()));
				conn.setDoOutput(true);
				conn.getOutputStream().write(postDataBytes);
				conn.getOutputStream().flush();

				in = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
				while ((c = in.read()) > -1);
				return nothing;
			} catch(Exception x) {
				Log.i(getPackageName(), "FUBAR FUBAR FUBAR FUBAR");
				Log.i(getPackageName(), x.toString());
				return nothing;
			}
		}

		protected void onPostExecute(String result) {
			/****/
		}

	} // end CallAPI

}

package org.takle;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;

@Path("/wisdom")
public class QuoteThingy {
	private static final String WISDOM_FILE = "/usr/share/doc/wisdom.txt";
	private static ArrayList<String>wisdom = null;
	@GET
	@Produces("text/plain")
	public String spewSomething(@Context HttpServletResponse response) {
		//response.addHeader("Access-Control-Allow-Origin", "http://www.takle.org");
        //response.addHeader("Access-Control-Allow-Credentials", "true");
        //response.addHeader("Access-Control-Allow-Methods", "GET");
        //response.addHeader("Access-Control-Allow-Headers", "Accept,Authorization,Cache-Control,Content-Type,DNT,If-Modified-Since,Keep-Alive,Origin,User-Agent,X-Mx-ReqToken,X-Requested-With");

		return getRandomChunkOfWisdom();
	}

	private synchronized String getRandomChunkOfWisdom() {
		BufferedReader r = null;
		String wrk;
		int idx = 0;
		if (wisdom == null) {
			wisdom = new ArrayList<String>();
			try {
				r = new BufferedReader(new FileReader(WISDOM_FILE));
				while ((wrk = r.readLine()) != null) {
					if (!wrk.startsWith("#")) {
						wisdom.add(wrk);
					}
				}
			} catch(Exception x) {
				x.printStackTrace();
				wisdom.add("I know nothing! - Sgt. Schultz");
			} finally {
				if (r != null) {
					try {
						r.close();
					} catch(Exception debris) { /****/ }
				}
			}
		}
		
		idx = (int)(Math.random() * wisdom.size());
		return wisdom.get(idx);
	}

}

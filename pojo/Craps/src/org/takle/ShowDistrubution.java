package org.takle;

import java.util.HashMap;
import java.util.Iterator;

// Yes I know the name of the class is mis-spelled
public class ShowDistrubution {
	public static final int ROLL_COUNT = 1000000;
	
	public static void main(String[] args) {
		(new ShowDistrubution()).createDistribution();
	}

	private void createDistribution() {
		int i, d1, d2, total, pct;
		String key;
		Integer val;
		HashMap<String, Integer> results = new HashMap<String, Integer>();
		Iterator<String> it;
		
		for (i = 0; i < ROLL_COUNT; i++) {
			d1 = rollTheDice();
			d2 = rollTheDice();
			total = d1 + d2;
			key = Integer.toString(total);
			if (results.containsKey(key)) {
				val = new Integer(results.get(key).intValue() + 1);
			} else {
				val = new Integer(1);
			}
			results.put(key, val);
		}

		for (i = 2; i <= 12; i++) {
			key = Integer.toString(i);
			pct = results.get(key).intValue() * 100 / ROLL_COUNT;
			System.out.println(key + " => " + pct);
		}
	}
	private int rollTheDice() {
		return ((int)(Math.random() * 6.0) + 1);
	}
}

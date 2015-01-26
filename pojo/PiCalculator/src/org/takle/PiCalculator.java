package org.takle;

public class PiCalculator {

	public static void main(String[] args) {
		long iterationCounter = 0;
		long denominator = 1;
		double currentPi = 0;
		double term;
		double percentage;
	
		while (denominator < Long.MAX_VALUE) {
			term = (double)4 / (double)denominator;

			if (iterationCounter % 2 == 0) {
				currentPi += term;
			} else {
				currentPi -= term;
			}

			denominator += 2;
			if (iterationCounter % 1000000000 == 0) {
				percentage = ((double)denominator * (double)100 / (double)Long.MAX_VALUE);
				System.out.println(denominator + " of " + Long.MAX_VALUE + "\t" + currentPi);
			}
		
			iterationCounter++;
		}

		System.out.println();
		System.out.println("Iteration count: " + iterationCounter);
		System.out.println("             PI: " + currentPi);
	}

}

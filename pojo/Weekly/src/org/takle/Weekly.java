package org.takle;

import java.util.Calendar;
import java.util.Date;

public class Weekly {
	private String[] MONTH = {
			"January",
			"Feburary",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December",
	};
	private final static int WEEK_COUNT = 53;
	private Calendar cal; 

	public static void main(String[] args) {
		(new Weekly()).process();
	}

	private boolean process() {
		try {
			int weekIdx = 0;
			initCal();
		
			openHTML();
			while (cal.get(Calendar.YEAR) < 2016) {
				printWeek(weekIdx + 1);
				weekIdx++;
			}
			closeHTML();
			return true;
		} catch(Exception x) {
			return false;
		}
	}

	private final String openEvenTD = "<td align='center' bgcolor='#dddddd'>";
	private final String openOddTD = "<td align='center' bgcolor='#cccccc'>";
	private final String openGenericTD = "<td align='center' bgcolor='#7777ff'>";
	private final String closeTD = "</td>";
	private final String openTR = "<tr>";
	private final String closeTR = "</tr>";
	private final String br = "<br/>";

	private void printWeek(int weekNum) {
		String openTD;
		int currentDayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
		int currentWeekOfYear = cal.get(Calendar.WEEK_OF_YEAR);
		String currentMonthName = MONTH[cal.get(Calendar.MONTH)];
		System.out.print(openTR);
		System.out.print(openGenericTD + weekNum + closeTD);

		while (currentDayOfWeek < 7) {
			currentDayOfWeek = cal.get(Calendar.DAY_OF_WEEK);
			currentMonthName = (MONTH[cal.get(Calendar.MONTH)]).substring(0, 3);
			if (cal.get(Calendar.MONTH) % 2 == 0) {
				openTD = openEvenTD;
			} else {
				openTD = openOddTD;
			}
			System.out.print(openTD + cal.get(Calendar.DAY_OF_MONTH) + br + currentMonthName + closeTD);
			cal.add(Calendar.DAY_OF_YEAR, 1);
		}

		currentMonthName = MONTH[cal.get(Calendar.MONTH)];
		System.out.println(closeTR);
	}

	private void openHTML() {
		System.out.println("<html>");
		System.out.println("<style>");
		System.out.println("td {");
		System.out.println("font-family: 'Courier'; color: #333333;");
		System.out.println("}");

		System.out.println("</style>");
		System.out.println("<body>");
		System.out.println("<div align='center'>");
		System.out.println("<table border='0' width='60%'>");
		System.out.println("<tr>");
		System.out.println("<td bgcolor='#7777ff' align='center'>#</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Sunday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Monday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Tuesday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Wednesday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Thursday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Friday</td>");
		System.out.println("<td bgcolor='#7777ff' align='center'>Saturday</td>");
		System.out.println("</tr>");
	}
	
	private void closeHTML() {
		System.out.println("</table>");
		System.out.println("</div>");
		System.out.println("</body>");
		System.out.println("</html>");
	}

	private void initCal() {
		Date d = new Date(2014, 11, 2);
		cal = Calendar.getInstance();
		cal.set(Calendar.DAY_OF_YEAR, 1);
		cal.add(Calendar.DAY_OF_YEAR, -4);
	}
}

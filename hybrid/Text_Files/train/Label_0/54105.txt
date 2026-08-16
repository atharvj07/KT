import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner stdin = new Scanner(System.in);
		
	
		String contest = stdin.next();
		String arrange = stdin.next();
		int[] dateC = makeDate(contest);
		int[] dateBob = makeDate(arrange);
		boolean age = false;
		for (int i=0; i<6; i++) {
			int[] newDate = new int[3];
			newDate[0] = dateBob[i/2]; 			  				  // 0, 0, 1, 1, 2, 2
			if (i < 3)
				newDate[1] = dateBob[(i+1)%3];                    // 1, 2, 0, 2, 0, 1
			else
				newDate[1] = dateBob[(i+2)%3];
			if (i ==0 || i== 5)									  // 2, 1, 2, 0, 1, 0
				newDate[2] = dateBob[2-i%3];
			else
				newDate[2] = dateBob[i%3];
				
			if (isValid(newDate)) {
				if (old(newDate, dateC))
					age = true;
			}
			
			//System.out.println(newDate[0]+" "+newDate[1]+" "+newDate[2]);
		}
		
		if (age)
			System.out.println("YES");
		else
			System.out.println("NO");
			
	}
	
	public static int[] makeDate(String d) {
		int[] date = new int[3];
		date[0] = (d.charAt(0) - '0')*10 + (d.charAt(1) - '0');
		date[1] = (d.charAt(3) - '0')*10 + (d.charAt(4) - '0');
		date[2] = (d.charAt(6) - '0')*10 + (d.charAt(7) - '0');
		return date;
	}
	
	public static boolean isValid(int[] d) {
		
		int[] daysreg = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		int[] daysleap = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		
		if (d[2]%4 == 0) {
			if (d[1] <= 12 && d[0] <= daysleap[d[1]-1])
				return true;
			else
				return false;	
		}
		else {
			if (d[1] <= 12 && d[0] <= daysreg[d[1]-1])
				return true;
			else
				return false;				
		}
	}
	
	public static boolean old(int[] d1, int[] d2) {
		// by year
		int age = d2[2] - d1[2];
		
		if (d2[1] < d1[1])
			age--;
		else if (d2[1] == d1[1] && d2[0] < d1[0] )
			age--;
		
		return (age >= 18);
	}
}


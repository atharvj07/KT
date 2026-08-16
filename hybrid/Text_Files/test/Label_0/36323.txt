import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = null;
		while((input = br.readLine()) != null){
			String[] v = input.split(" ");
			int year = Integer.parseInt(v[0]);
			int month = Integer.parseInt(v[1]) - 1;	// 0 <= month <= 11
			int date = Integer.parseInt(v[2]);
			String era = transToEra(new GregorianCalendar(year, month, date));
			System.out.println(era + ((era.equals("pre-meiji"))? "": " " + (month + 1) + " " + date));
		}
	}

	public static String transToEra(GregorianCalendar date){
		GregorianCalendar startMeiji = new GregorianCalendar(1868, Calendar.SEPTEMBER, 8);
		GregorianCalendar startTaisho = new GregorianCalendar(1912, Calendar.JULY, 30);
		GregorianCalendar startShowa = new GregorianCalendar(1926, Calendar.DECEMBER, 25);
		GregorianCalendar startHeisei = new GregorianCalendar(1989, Calendar.JANUARY, 8);
		final int yearField = Calendar.YEAR;
		if(date.before(startMeiji)){
			return "pre-meiji";
		}else if(date.before(startTaisho)){
			return "meiji " + (date.get(yearField) - startMeiji.get(yearField) + 1);
		}else if(date.before(startShowa)){
			return "taisho " + (date.get(yearField) - startTaisho.get(yearField) + 1);
		}else if(date.before(startHeisei)){
			return "showa " + (date.get(yearField) - startShowa.get(yearField) + 1); 
		}else{
			return "heisei " + (date.get(yearField) - startHeisei.get(yearField) + 1);
		}
	}
}
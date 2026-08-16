import java.util.Scanner;

class Main {
	public static void main(String[] args){
		
		Scanner input = new Scanner(System.in);
		
		while (true){
			int year1, month1, date1;
			
			year1 = input.nextInt();
			if (year1 < 0)return;
			
			month1 = input.nextInt();
			if (month1 < 0)return;
			
			date1 = input.nextInt();
			if (date1 < 0)return;
			
			Day d1 = new Day(year1, month1, date1);
			
			int year2, month2, date2;
			
			year2 = input.nextInt();
			if (year2 < 0)return;
			
			month2 = input.nextInt();
			if (month2 < 0)return;
			
			date2 = input.nextInt();
			if (date2 < 0)return;
			
			Day d2 = new Day(year2, month2, date2);
			
			
			int[] md = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
			int[] ml = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
			
			int sumday = 0;
			
			
			for (int i = year1; i < year2; i++){
				if ( i % 400 == 0 || (i % 4 == 0 && i % 100 != 0))sumday += 366;
				else sumday += 365;
			}
			
			
			for (int i = 1; i < month1; i++){
				if ( year1 % 400 == 0 || (year1 % 4 == 0 && year1 % 100 != 0))sumday -= ml[i];
				else sumday -= md[i];
			}
			
			for (int i = 1; i < month2; i++){
				if ( year2 % 400 == 0 || (year2 % 4 == 0 && year2 % 100 != 0))sumday += ml[i];
				else sumday += md[i];
			}
			
			sumday -= date1;
			sumday += date2;
			
			
			System.out.println(sumday);
		}
	}
}

class Day {
	private int year;
	private int month;
	private int date;
	
	public Day(int year, int month, int date) {
		this.year = year;
		this.month = month;
		this.date = date;
	}
	
	public Day() {}
	
	public void printDay(){
		System.out.println("year = " + this.year);
		System.out.println("month = " + this.month);
		System.out.println("date = " + this.date);
	}
	
	public void setYear(int year){
		this.year = year;
	}
	
	public void setMonth(int month){
		this.month = month;
	}
	
	public void setDate(int date){
		this.date = date;
	}
	
	public int getYear(){
		return year;
	}
	
	public int getMonth(){
		return month;
	}
	
	public int getDate(){
		return date;
	}
}
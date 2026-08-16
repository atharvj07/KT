import java.util.Scanner;

class Main {
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		double speed;
		int floor;
		
		while(scan.hasNextDouble()){
			speed = scan.nextDouble();
			floor = (int)Math.ceil(((4.9*(speed/9.8)*(speed/9.8))+5)/5);
			
			System.out.println(floor);
		}
	}
}
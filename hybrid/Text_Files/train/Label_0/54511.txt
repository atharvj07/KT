import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	int l = input.nextInt();
	int p = input.nextInt();
	int q = input.nextInt();

	double collisionT = ((double)l)/(p+q);
	double harryDistance = collisionT*p;


	double collisionT2 = ((double)(l*2))/(p+q);
	double harryDistance2 = collisionT2*p;


	double distance = harryDistance2-harryDistance;

	System.out.println(distance);
    }
}
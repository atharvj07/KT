import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		Dice d = new Dice(scan.nextInt(), scan.nextInt(), scan.nextInt(), scan.nextInt(), scan.nextInt(),
				scan.nextInt());
		String op = scan.next();
		for (int i = 0; i < op.length(); i++)
			d.operate(op.charAt(i));
		System.out.println(d.getUpp());

		scan.close();
		System.exit(0);
	}

}

class Dice {
	int Upp, Sou, Est, Wst, Nor, Bot;

	public Dice(int upp, int sou, int est, int wst, int nor, int bot) {
		Upp = upp;
		Sou = sou;
		Est = est;
		Wst = wst;
		Nor = nor;
		Bot = bot;
	}

	public void operate(char op) {
		int tmp;
		switch (op) {
		case 'S':
			tmp = Upp;
			Upp = Nor;
			Nor = Bot;
			Bot = Sou;
			Sou = tmp;
			break;
		case 'E':
			tmp = Upp;
			Upp = Wst;
			Wst = Bot;
			Bot = Est;
			Est = tmp;
			break;
		case 'W':
			tmp = Upp;
			Upp = Est;
			Est = Bot;
			Bot = Wst;
			Wst = tmp;
			break;
		case 'N':
			tmp = Upp;
			Upp = Sou;
			Sou = Bot;
			Bot = Nor;
			Nor = tmp;
			break;
		}
	}

	public int getUpp() {
		return Upp;
	}

}
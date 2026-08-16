import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {
		// BufferedReader stdIn = new BufferedReader(new FileReader(new
		// File("c:\\2024-input.txt")));

		BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
		String s;
		while ((s = stdIn.readLine()) != null) {
			int setc = Integer.valueOf(s);
			for (int i = 0; i < setc; i++) {
				// read initial cards and deal cards
				String ini = stdIn.readLine();
				String deal = stdIn.readLine();
				String[] inis = ini.split(" ");
				String[] deals = deal.split(" ");
				// process dealers action
				Dealer d = new Dealer(inis);
				d.action(deals);
			}
		}
		System.exit(0);
	}
}

class Dealer {
	private int score = 0;
	private int ace11 = 0;
	private int piece = 0;

	// first 2 cards
	Dealer(String[] inis) {
		this.addcard(inis[0]);
		this.addcard(inis[1]);
	}

	// hits card until stand, and output result. otherwise
	public void action(String[] deals) {
		for (int i = 0; this.isHit(); i++)
			this.addcard(deals[i]);
		;
		if (score == 21 && piece == 2)
			System.out.println("blackjack");
		else if (score > 21)
			System.out.println("bust");
		else
			System.out.println(score);

	}

	// judge hits or stand
	private boolean isHit() {
		if (score > 21 && ace11 > 0) {
			score -= 10;
			--ace11;
			return (isHit());
		}
		if (score == 17 && ace11 > 0)
			return true;
		if (score > 16)
			return false;
		else
			return true;
	}

	// hits one card
	private void addcard(String s) {
		switch (s) {
		case ("A"):
			score += 11;
			ace11 += 1;
			break;
		case ("T"):
		case ("J"):
		case ("Q"):
		case ("K"):
			score += 10;
			break;
		default:
			score += Integer.valueOf(s);
			break;
		}
		piece += 1;
	}
}
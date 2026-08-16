import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
	static class Word implements Comparable<Word>{
		String word;
		int cnt;

		Word(String word) {
			this.word = word;
			cnt = 1;
		}

		public int compareTo(Word o) {
			return o.cnt == this.cnt ? this.word.compareTo(o.word) : o.cnt - this.cnt;
		}
	}

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n;

		while (true) {
			n = sc.nextInt();
			if (n == 0) {
				break;
			}
			sc.nextLine();
			String str[][] = new String[n][];
			for (int i = 0; i < n; i++) {
				str[i] = sc.nextLine().split(" ");
			}

			char cc[] = sc.nextLine().toCharArray();
			int c = cc[0];

			Word w[] = new Word[600 * n];
			LinkedList<String> list = new LinkedList<String>();
			int id = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < str[i].length; j++) {
					if (str[i][j].charAt(0) == c) {
						if (!list.contains(str[i][j])) {
							list.add(str[i][j]);
							w[id] = new Word(str[i][j]);
							id++;
						} else {
							for (int k = 0; k < id; k++) {
								if (w[k].word.equals(str[i][j])) {
									w[k].cnt++;
									break;
								}
							}
						}
					}
				}
			}

			Arrays.sort(w, 0, id);
			if (id == 0) {
				System.out.println("NA");
			} else {
				String s = "";
				for (int i = 0; i < 5 && i < id; i++) {
					System.out.print(s + w[i].word);
					s = " ";
				}
				System.out.println();
			}
		}
	}
}
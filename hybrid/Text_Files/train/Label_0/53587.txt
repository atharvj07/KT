
import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	Scanner sc;

	void println(String alg) {
//		System.err.println(alg);
	}

	class exp {
		int type = 0;
		long value;
		String arr;
		exp chi;

		exp(String buffer) {
			println("e " + buffer);
			int index = buffer.indexOf('[');

			if (index == -1) {
				type = 1;
				value = Long.valueOf(buffer);
			} else {
				arr = buffer.charAt(0) + "";
				chi = new exp(buffer.substring(2, buffer.length() - 1));
			}
		}

		boolean det = false;

		long valueOf() {
			if (det) {
				return value;
			} else {
				if (type == 1) {
					det = true;
					return value;
				} else {
					long v2 = chi.valueOf();

					if (v2 == -1) {
						det = true;
						return -1;
					}

					String key = arr + v2;

					if (Main.this.value.containsKey(key)) {
						long v = Main.this.value.get(key);
						det = true;
						value = v;
						return value;
					}
				}
			}
			return -1;
		}
	}

	class ass {
		String arr;
		exp e1;
		exp e2;

		ass(String buffer) {
			println("a " + buffer);
			String[] a = buffer.split("=");

			arr = a[0].charAt(0) + "";
			e1 = new exp(a[0].substring(2, a[0].length() - 1));
			e2 = new exp(a[1]);
		}

		boolean valid() {
			long l3 = e2.valueOf();
			if (l3 != -1) {
				long l2 = e1.valueOf();
				if (l2 != -1) {
					if (ary.containsKey(arr)) {
						long l = ary.get(arr);
						if (l2 < l) {
							value.put(arr + e1.valueOf(), e2.valueOf());
							return true;
						}
					}
				}
			}
			return false;
		}
	}

	class dec {
		String a;
		long value;

		dec(String buffer) {
			println("d " + buffer);
			a = buffer.charAt(0) + "";
			value = Long.valueOf(buffer.substring(2, buffer.length() - 1));
		}

		boolean valid() {
			if (ary.containsKey(a)) {
				return false;
			} else {
				ary.put(a, value);
			}
			return true;
		}
	}

	class line {
		int type = 0;
		ass as;
		dec dc;

		line(String buffer) {
			println("l " + buffer);
			if (buffer.contains("=")) {
				type = 1;
				as = new ass(buffer);
			} else {
				type = 0;
				dc = new dec(buffer);
			}
		}

		boolean valid() {
			if (type == 1) {
				return as.valid();
			} else {
				return dc.valid();
			}
		}
	}

	HashMap<String, Long> ary = new HashMap<String, Long>();
	HashMap<String, Long> value = new HashMap<String, Long>();

	void run() {
		for (;;) {
			ary.clear();
			value.clear();
			
			int min = 123456;
			{
				String buffer = sc.nextLine();
				if (buffer.equals(".")) {
					break;
				}

				line l = new line(buffer);
				if (!l.valid()) {
					min = Math.min(min, 1);
				}
			}
			for (int i = 2;; i++) {
				String buffer = sc.nextLine();
				if (buffer.equals(".")) {
					break;
				}

				line l = new line(buffer);
				if (!l.valid()) {
					min = Math.min(min, i);
				}
			}
			if (min == 123456) {
				System.out.println(0);
			} else {
				System.out.println(min);
			}
		}
	}

	Main() {
		sc = new Scanner(System.in);
		try {
			sc = new Scanner(new File(""));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			// e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		new Main().run();
	}
}
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String var;
		String type;

		while (true) {
			var = sc.next();
			type = sc.next();
			if (type.equals("X")) {
				break;
			}

			int n = 0;
			for (int i = 0; i < var.length(); i++) {
				if (var.charAt(i) == '_') {
					n = 3;
				}
			}
			if (n != 3) {
				if ('A' <= var.charAt(0) && var.charAt(0) <= 'Z') {
					n = 1;
				} else if ('a' <= var.charAt(0) && var.charAt(0) <= 'z') {
					n = 2;
				}
			}

			if (type.equals("U")) {
				if (n == 1) {
				} else if (n == 2) {
					String v = var.substring(0, 1);
					v = v.toUpperCase();
					var = v + var.substring(1);
				} else {
					String v = var.substring(0, 1);
					v = v.toUpperCase();
					var = v + var.substring(1);
					for (int i = 0; i < var.length(); i++) {
						if (var.charAt(i) == '_') {
							v = var.substring(i + 1, i + 2);
							v = v.toUpperCase();
							var = var.substring(0, i) + v + var.substring(i + 2);
							i--;
						}
					}
				}
			} else if (type.equals("L")) {
				if (n == 1) {
					String v = var.substring(0, 1);
					v = v.toLowerCase();
					var = v + var.substring(1);
				} else if (n == 2) {
				} else {
					for (int i = 0; i < var.length(); i++) {
						if (var.charAt(i) == '_') {
							String v = var.substring(i + 1, i + 2);
							v = v.toUpperCase();
							var = var.substring(0, i) + v + var.substring(i + 2);
							i--;
						}
					}
				}
			} else if (type.equals("D")) {
				if (n == 1) {
					String v = var.substring(0, 1);
					v = v.toLowerCase();
					var = v + var.substring(1);
					for (int i = 0; i < var.length(); i++) {
						if ('A' <= var.charAt(i) && var.charAt(i) <= 'Z') {
							v = var.substring(i, i + 1);
							v = v.toLowerCase();
							var = var.substring(0, i) + '_' + v + var.substring(i + 1);
						}
					}
				} else if (n == 2) {
					for (int i = 0; i < var.length(); i++) {
						if ('A' <= var.charAt(i) && var.charAt(i) <= 'Z') {
							String v = var.substring(i, i + 1);
							v = v.toLowerCase();
							var = var.substring(0, i) + '_' + v + var.substring(i + 1);
						}
					}
				} else {
				}
			}
			System.out.println(var);
		}
	}
}
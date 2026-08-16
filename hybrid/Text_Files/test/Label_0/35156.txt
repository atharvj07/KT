import java.util.Scanner;
class Main {
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)) {
			// unsigned int
			long a = sc.nextLong();
			long b = sc.nextLong();

			System.out.println(toPaddedBinaryString(a&b));
			System.out.println(toPaddedBinaryString(a|b));
			System.out.println(toPaddedBinaryString(a^b));
		}
	}
	/**
	 * 0パディングするのである
	 * @param bin バイナリするlong
	 * @return
	 */
	public static String toPaddedBinaryString(long bin) {
		String result = String.format("%32s", Long.toBinaryString(bin)).replaceAll(" ", "0");
		if(result.length()>32)
			return result.substring(result.length()-32);
		return result;
	}
}

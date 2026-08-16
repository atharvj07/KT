import java.io.PrintWriter;
import java.util.*;

public class Main {
	public static String implementation(List<String> array){
		int n = Integer.parseInt(array.get(0));
		String a = array.get(1);
		String b = array.get(2);
		String c = array.get(3);

		int count = 0;
		for(int i=0; i<n; i++){
			if(a.charAt(i)==b.charAt(i) && a.charAt(i)==c.charAt(i)){
				// Do nothing
			} else if (a.charAt(i)==b.charAt(i) || b.charAt(i)==c.charAt(i) || c.charAt(i)==a.charAt(i)) {
				count += 1;
			} else {
				count +=2;
			}
		}
		return String.valueOf(count);
	}

	public static void main(String[] args){
		// Input
		Scanner sc = new Scanner(System.in);

		// Read input and execute method
		String tmp;
		List<String> array = new ArrayList<String>();
		while(true) {
			try {
				tmp = sc.nextLine();
				if (tmp.length() == 0) {
					exec(array);
					array.clear();
				} else {
					array.add(tmp);
				}
			} catch (Exception e){
				exec(array);
				break;
			}
		}
	}

	public static void exec(List<String> array){
		// Output variable
		String out = implementation(array);

		// Output
		PrintWriter stdOut = new PrintWriter(System.out);
		stdOut.println(out);
		stdOut.flush();

		// Debug
		if(array.get(array.size()-1).startsWith("a:")) {
			if (!array.get(array.size() - 1).substring(2).equals(out)) {
				System.out.println("error included");
				System.out.println("output : " + out);
				System.out.println("expected : " + array.get(array.size()-1).substring(2));
			} else {
				System.out.println("correct answer!!");
			}
			System.out.println("");
		}
	}
}

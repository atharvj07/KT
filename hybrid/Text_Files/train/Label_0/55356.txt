import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	private	static	BufferedReader	br = null;

	static {
		br = new BufferedReader(new InputStreamReader(System.in));
	}
 
    /**
     * @param args
     */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int 	cnt = parseNum();
		int[]	frq = new int[6];

		while (cnt-- > 0) {
			frq[parseRank()]++;
		}

		for (int i = 0; i < frq.length; i++) {
			String	out = (i+1) + ":";

			while(frq[i] > 0) {
				out += "*";
				frq[i]--;
			}

			System.out.println(out);
		}
	}
 
	private static int parseRank() {
		int		rank = 5;
		double	data = Double.parseDouble(parseStdin());

		if (data < 165.0) {
			rank = 0;
		}
		else if (data < 170.0) {
			rank = 1;
		}
		else if (data < 175.0) {
			rank = 2;
		}
		else if (data < 180.0) {
			rank = 3;
		}
		else if (data < 185.0) {
			rank = 4;
		}

		return rank;
	}
 
	private static int parseNum() {
		int     num = 0;
		String  str = null;

		if ((str = parseStdin()) != null) {
			num = Integer.parseInt(str);
		}

		return num;
	}
 
	private static String parseStdin() {
        String  stdin = null;
        
        try {
        	String  tmp = br.readLine();
        	if (tmp != null) {
            	if (!tmp.isEmpty()) stdin = tmp;
        	}
        }
        catch (IOException e) {}
 
        return stdin;
	}
}
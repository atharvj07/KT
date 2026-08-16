import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
	private	static	BufferedReader		br      = null;
	private	static	ArrayList<Integer>	borders = null;

	static {
		br      = new BufferedReader(new InputStreamReader(System.in));
		borders = new ArrayList<Integer>();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		parseBorder();
		short[]	sum = createSumList();

		int nLen = borders.size();
		for (int n = 0; n < nLen; n++) {
			System.out.println(sum[borders.get(n)-1]);
		}
	}

	private static void parseBorder() {
		int	nNum = 0;
		while((nNum = parseNum()) != 0) {
			borders.add(nNum);
		}
	}

	private static int parseNum() {
		int		num    = 0;
		String	strNum = parseStdin();

		if (strNum != null) {
			num = Integer.parseInt(strNum);
		}

		return num;
	}

	private static String parseStdin() {
		String	strNum = null;

		try {
			String line = br.readLine();
			if (line != null) {
				if (!line.isEmpty()) {
					strNum = line;
				}
			}
		}
		catch (IOException e) {}

		return strNum;
	}

	private static short[] createSumList() {
		short[]				aSum   = null;
		ArrayList<Integer>	prime = new ArrayList<Integer>();
		boolean				bPrime = true;
		int					nPrime = 0;
		Object[]			aWork  = borders.toArray();
		int					nPr1   = 0;
		int					nPr2   = 0;
		int					nLen   = 0;
		int					nMax   = 0;

		Arrays.sort(aWork);
		nMax = (Integer)aWork[aWork.length - 1];

		prime.add(2);
		for(int nNum = 3; nNum <= nMax; nNum += 2) {
			bPrime = true;

			for (int nLoop = 0; nLoop < prime.size(); nLoop++) {
				nPrime = prime.get(nLoop);
				if (nPrime <= (int)Math.sqrt((double)nNum)) {
					if (nNum % nPrime == 0) {
						bPrime = false;
						break;
					}
				}
				else {
					break;
				}
			}

			if (bPrime) {
				prime.add(nNum);
			}
		}

		aSum = new short[nMax];
		nLen = prime.size();
		for (int a = 0; a < nLen; a++) {
			nPr1 = prime.get(a);
			if (nPr1 > nMax / 2 + nMax % 2) {
				break;
			}
			for (int b = a; b < nLen; b++) {
				nPr2 = prime.get(b);
				if (nPr1 + nPr2 > nMax) {
					break;
				}
				aSum[nPr1 + nPr2 - 1]++;
			}
		}

		return aSum;
	}
}
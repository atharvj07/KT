import java.util.*;

public class Main{
	public static void main(String[] args){

		Scanner scan = new Scanner(System.in);

		int h = scan.nextInt();
		int w = scan.nextInt();
		String[] t = new String[h];
		for(int i = 0; i < h; i++)
			t[i] = scan.next();

		int r = scan.nextInt();
		int c = scan.nextInt();
		String[] p = new String[r];
		for(int i = 0; i < r; i++)
			p[i] = scan.next();

		PtFind f = new PtFind(t, p, false);

		scan.close();
		System.exit(0);
	}
}

class PtFind{
	boolean debug;

	public PtFind(String[] t, String[] p, boolean d){
		debug = d;

		boolean[][] jg = new boolean[t.length - p.length + 1][t[0].length() - p[0].length() + 1];
		//length????????????????´???°???length()??????????????°
		for(int y = 0; y < jg.length; y++)
			for(int x = 0; x < jg[0].length; x++)
				jg[y][x] = true; //true?????£??\??????

		for(int r = 0; r < p.length; r++){
			StFind stf = new StFind(p[r], d);
			for(int y = 0; y < jg.length; y++){
				boolean[] result = new boolean[jg[0].length];
				stf.find(t[y+r], p[r], result);
				for(int x = 0; x < jg[0].length; x++)
					jg[y][x] &= result[x];
					//a &= b??????a = a & b
			}
		}

		for(int y = 0; y < jg.length; y++)
			for(int x = 0; x < jg[0].length; x++)
				if(jg[y][x])
					System.out.println(y + " " + x);
	}
}

//
class StFind{
	boolean debug;
	int[] msft;
	int[] sft = new int[Character.MAX_CODE_POINT];

	public StFind(String p, boolean d){
		debug = d;
		createMatchPt(p);
	}

	public void find(String t, String p, boolean[] result){
		int x = 0;
		for(int st = 0; st < t.length() - p.length() + 1;){
			if((x = isBaEqual(t, p, st)) == p.length())
				result[st] = true;
			st += msft[x];
		}
	}

	private void createMatchPt(String p){
		msft = new int[p.length() + 1];
		msft[0] = p.length();

		for(int sft = p.length(); sft > 0; sft--){
			for(int m = 1; m < msft.length; m++){
				if(m > p.length() - sft){
					msft[m] = sft;
					continue;
				}
				if(p.charAt(p.length() - m) != p.charAt(p.length() - m- sft)){
					msft[m-1] = sft;
					break;
				}else if(m == p.length() -sft)
					msft[m] = sft;
			}
		}

		if(debug)
			for(int i = 0; i < msft.length; i++)
				System.out.println("--- " + i + " : " + msft[i]);
	}

	//
	int stPre = 0;
	int retPre = 0;

	private int isBaEqual(String t, String p, int st){
		int clen = p.length();
		int stlen = stPre + p.length();
		if(st >= stlen - retPre && st < stlen){
			clen -= stlen - st;
		}
		/*
		if(st >= stPre + p.length() - retPre && st < stPre + p.length()){
		
			clen -= stPre + p.length() - st;
		}
		*/
		for(int i = 0; i < clen; i++){
			if(t.charAt(p.length() - 1 - i + st) != p.charAt(p.length() - 1 - i)){
				stPre = st;
				retPre = i;
				return i;
			}
		}
		stPre = st;
		retPre = p.length();
		return p.length();
	}
}
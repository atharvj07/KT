import java.io.*;
import java.util.*;
import java.math.*;

class Main{
	static final int nbits = 64;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw = new PrintWriter(System.out);
		String[] str = br.readLine().split(" ");
		int q = Integer.parseInt(str[0]);
		BitSet bs = new BitSet(nbits);
		for(int i = 0; i < q; i++){
			str = br.readLine().split(" ");
			int op = Integer.parseInt(str[0]);
			if(op >= 0 && op <= 3){
				int pos = Integer.parseInt(str[1]);
				if(op == 0){
					pw.println(bs.get(pos) ? 1 : 0);
				}else if(op == 1){
					bs.set(pos);
				}else if(op == 2){
					bs.clear(pos);
				}else{
					bs.flip(pos);
				}
			}else{
				if(op == 4){
					boolean flag = true;
					for(int j = 0; j < nbits; j++) flag &= bs.get(j);
					pw.println(flag ? 1 : 0);
				}else if(op == 5){
					pw.println(!bs.isEmpty() ? 1 : 0);
				}else if(op == 6){
					pw.println(bs.isEmpty() ? 1 : 0);
				}else if(op == 7){
					int cnt = 0;
					for(int j = 0; j < nbits; j++){
						if(bs.get(j)) cnt++;
					}
					pw.println(cnt);
				}else{
					BigInteger sum = BigInteger.ZERO;
					BigInteger pow2 = BigInteger.ONE;
					BigInteger TWO = BigInteger.ONE.add(BigInteger.ONE);
					for(int j = 0; j < nbits; j++){
						if(bs.get(j)) sum = sum.add(pow2);
						pow2 = pow2.multiply(TWO);
					}
					pw.println(sum);
				}
			}
		}
		pw.close();
	}
}


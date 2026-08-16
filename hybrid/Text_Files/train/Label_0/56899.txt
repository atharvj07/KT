import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO ?????????????????????????????????????????????
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n ; i++){
			String[] tmpArray = br.readLine().split(" ");
			
			int x1 = getIntFromMCXI(tmpArray[0]);
			int x2 = getIntFromMCXI(tmpArray[1]);
			//System.out.println(x1 + " " + x2);
			
			int result = x1 + x2;
			
			System.out.println(getMCXIfromInt(result));
		}
	}

	private static String getMCXIfromInt(int result) {
		// TODO ?????????????????????????????????????????????
		StringBuffer str = new StringBuffer();
		
		if(result >= 1000 && result < 2000){
			str.append("m");
		}
		else if(result >= 2000){
			str.append(result/1000 + "m");
		}
		
		if(result%1000 >= 100 && result%1000 < 200){
			str.append("c");
		}
		else if(result%1000 >= 200){
			str.append((result%1000)/100 + "c");
		}

		if(result%100 >= 10 && result%100 < 20){
			str.append("x");
		}
		else if(result%100 >= 20){
			str.append((result%100)/10 + "x");
		}
		
		if(result%10 >= 1 && result%10 < 2){
			str.append("i");
		}
		else if(result%10 >= 2){
			str.append((result%10) + "i");
		}
		
		return str.toString();
	}

	private static int getIntFromMCXI(String string) {
		// TODO ?????????????????????????????????????????????
		int result = 0;
		int indexM = string.indexOf('m');
		
		if(indexM == 0){
			result += 1000;
		}
		else if(indexM != -1){
			result += 1000*Integer.parseInt(string.substring(indexM - 1, indexM));
		}
		
		int indexC = string.indexOf('c');
		
		if(indexC == 0 || indexC >= 1 && Character.isAlphabetic(string.charAt(indexC - 1))){
			result += 100;
		}
		else if(indexC != -1){
			result += 100*Integer.parseInt(string.substring(indexC - 1, indexC));
		}

		int indexX = string.indexOf('x');
		
		if(indexX == 0 || indexX >= 1 && Character.isAlphabetic(string.charAt(indexX - 1))){
			result += 10;
		}
		else if(indexX != -1){
			result += 10*Integer.parseInt(string.substring(indexX - 1, indexX));
		}
		
		int indexI = string.indexOf('i');
		
		if(indexI == 0 || indexI >= 1 && Character.isAlphabetic(string.charAt(indexI - 1))){
			result += 1;
		}
		else if(indexI != -1){
			result += Integer.parseInt(string.substring(indexI - 1, indexI));
		}
		return result;
	}

}
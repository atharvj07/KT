import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO ?????????????????????????????????????????????
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		String[] array = input.split("[ .,]");
		
		boolean first = true;
		for(int i = 0; i < array.length ; i++){
			if(array[i].length() >= 3 && array[i].length() <= 6){
				if(!first){
					System.out.print(" ");
				}
				System.out.print(array[i]);
				first = false;
			}
		}
		System.out.println();
	}

}
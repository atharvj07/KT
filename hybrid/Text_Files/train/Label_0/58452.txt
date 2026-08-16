import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);

		List<Integer> list = new ArrayList<Integer>();
		list.add(1);
		list.add(2);
		list.add(4);
		list.add(8);
		list.add(16);
		list.add(32);
		list.add(64);
		list.add(128);
		list.add(256);
		list.add(512);

		while (sc.hasNext()){

			int num = sc.nextInt();

			List<Integer> outputList = new ArrayList<Integer>();

			for(int i = list.size() - 1; i >= 0; i--){

				if(num == 0) break;

				if(num >= list.get(i)){
					num -= list.get(i);

					outputList.add(list.get(i));
				}
			}
			Collections.sort(outputList);

			for(int i = 0; i < outputList.size() - 1; i++){
				System.out.print(outputList.get(i) + " ");
			}

			System.out.println(outputList.get(outputList.size() - 1));
		}
	}

}
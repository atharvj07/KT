import java.util.Scanner;
import java.util.SortedMap;
import java.util.TreeMap;

class Main {

	public static void main(String[] args) {
		try (Scanner sc = new Scanner(System.in)){
			int times = sc.nextInt();
			TreeMap<Long, Long> map = new TreeMap<>();
			long size = 0l;
			for (int i = 0; i<times; i++){
				int query = sc.nextInt();  //0insert 1find 2delete 3dump
				long x = sc.nextLong();
				switch (query) {
				//insert(x)
				case 0:
					if (!map.containsKey(x)) map.put(x,1l);
					else map.put(x,map.get(x)+1);
					size++;  //毎回size+1
					System.out.println(size);
					break;
				//find(x)
				case 1:
					if (map.get(x)!=null) {
						System.out.println(map.get(x));
					} else System.out.println(0);
					break;
				//delete(x)
				case 2:
					if (map.get(x) != null) {
						size -= map.get(x);  //remove時sizeを減る
						map.remove(x);
					}
					break;
				//dump(x,large)
				case 3:
					long large = sc.nextLong();
					SortedMap<Long,Long> submap = map.subMap(x,true,large,true);
					for (Long l : submap.keySet()) {
						for (int j=0; j<map.get(l); j++) System.out.println(l);   //回数があるだけ出力
					}
					break;
				}
			}
		}
	}
}

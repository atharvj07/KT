import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main{
	static final int LARGE = 3;
	static final int MIDDLE = 2;
	static final int SMALL = 1;
	
	static int N = 0;
	static String[] answer = null;
	
	public static void main(String[] args) {
		int[] map = new int[10 * 10];
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		List<String> inputDataList = new ArrayList<String>();
		String input = null;

		try {
			while ((input = in.readLine()) != null) {
				inputDataList.add(input.trim());
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		N = Integer.parseInt(inputDataList.get(0));
		for (int i = 0; i < 10; i++) {
			String[] array = inputDataList.get(i + 1).split(" ");
			for (int j = 0; j < 10; j++) {
				map[i * 10 + j] = Integer.parseInt(array[j]);
			}
		}
		inputDataList = null;
		
		String[] ans = new String[N];
		searchBluer(map, 0, 0, ans);
		for(String s : answer) {
			System.out.println(s);
		}
	}

	private static void searchBluer(int[] map, int n, int count, String[] ans) {
		if (map == null || answer != null) {
			return;
		}
		if (n == N ) {
			Arrays.sort(map);
			if(map[map.length - 1] == 0) {
				answer = ans.clone();
			}
			return;
		}
		
		while (map[count] < 1)
			count++;
		
		ArrayList<BlurParam> list = findType(map, count);

		for(BlurParam bp : list) {
			ans[n] = (bp.x) + " " + (bp.y) + " " + bp.size;
			searchBluer(updateMap(map, bp.x, bp.y, bp.size), n + 1, count, ans);
		}
	}

	private static ArrayList<BlurParam> findType(int[] clone, int count) {
		int x = count % 10;
		int y = count / 10;
		
		/*中心はこの時点で不明　可能性のあるパターンを全て試す*/
		ArrayList<BlurParam> list = new ArrayList<BlurParam>();

		list.addAll(chekcSmall(clone, x, y));
		list.addAll(chekcMiddle(clone, x, y));
		list.addAll(checkLarge(clone, x, y));
		
		return list;
	}

	private static ArrayList<BlurParam> checkLarge(int[] clone, int x, int y) {
		ArrayList<BlurParam> param = new ArrayList<BlurParam>();
		
		//上2
		if(y < 8 && clone[(y+2)*10 + x] != 0) {
			param.add( new BlurParam(x, y+2, LARGE));
		}
		//左2
		if(y == 0 && clone[y*10 + x+2] != 0) {
			param.add( new BlurParam(x+2, y, LARGE));
		}
		//左上
		if(y == 0 && clone[(y+1)*10 + x+1] != 0) {
			param.add( new BlurParam(x+1, y+1, LARGE));
		}
		//上 左　中心
		if(x == 0 && y == 0 &&clone[(y+1)*10+x] != 0 && clone[y*10 + x+1] != 0) {
			param.add( new BlurParam(x, y+1, LARGE));
			param.add( new BlurParam(x+1, y, LARGE));
			param.add( new BlurParam(x, y, LARGE));
		}
		return param;
	}

	private static ArrayList<BlurParam> chekcMiddle(int[] clone, int x, int y) {
		ArrayList<BlurParam> param = new ArrayList<BlurParam>();
		//左上
		if(clone[(y+1)*10 + x+1] != 0) {
			param.add( new BlurParam(x+1, y+1, MIDDLE));
		}
		//上
		if(x == 0 && clone[(y+1)*10+x] != 0) {
			param.add( new BlurParam(x, y+1, MIDDLE));
		}
		//左
		if(y == 0 && clone[y*10 + x+1] != 0) {
			param.add( new BlurParam(x+1, y, MIDDLE));
		}
		//中心
		if(x == 0 && y == 0) {
			param.add( new BlurParam(x, y, MIDDLE));
		}
		return param;
	}

	private static ArrayList<BlurParam> chekcSmall(int[] clone, int x, int y) {
		ArrayList<BlurParam> param = new ArrayList<BlurParam>();
		//上
		if(clone[(y+1)*10+x] != 0) {
			param.add( new BlurParam(x, y+1, SMALL));
		}
		//左
		if(y == 0 && clone[y*10 + x+1] != 0) {
			param.add( new BlurParam(x+1, y, SMALL));
		}
		//中心
		if(x == 0 && y == 0) {
			param.add( new BlurParam(x, y, SMALL));
		}
		return param;
	}

	private static int[] updateMap(int[] tmp, int x, int y, int size) {
		int[] clone = tmp.clone();
		switch(size) {
		case 3: if(x >= 2) clone[y*10 + x - 2]--;
				if(x <= 7) clone[y*10 + x + 2]--;
				if(y >= 2) clone[(y - 2)*10  + x]--;
				if(y <= 7) clone[(y + 2)*10 + x]--;
				
		case 2: // 左上
				if (x > 0 && y > 0)
				clone[(y - 1)*10 + x - 1]--;
				// 右上
				if (x < 9 && y > 0)
				clone[(y - 1)*10 + x + 1]--;
				// 左下
				if (y < 9 && x > 0)
				clone[(y + 1)*10 + x - 1]--;
				// 右下
				if (y < 9 && x < 9)
				clone[(y + 1)*10 + x + 1]--;
				
		case 1: if(x >= 1) clone[y*10 + x - 1]--;
				if(x <= 8) clone[y*10 + x + 1]--;
				if(y >= 1) clone[(y - 1)*10 + x]--;
				if(y <= 8) clone[(y + 1)*10 + x]--;
		}
		clone[y*10 + x]--;
		
		//途中経過
		/*
		System.out.println("" + x + " " + y + " " + size);

		for(int i = 1; i <= clone.length; i++) {
			System.out.print(clone[i-1] + " ");
			if(i % 10 == 0) 
				System.out.println();

		}
		*/
		int[] copy = clone.clone();
		Arrays.sort(copy);
		if(copy[0] < 0) {
			clone = null;
		}
		copy = null;
		return clone;
	}
}

class BlurParam{
	int x;
	int y;
	int size;
	
	public BlurParam(int _x, int _y, int _size) {
		x = _x;
		y = _y;
		size = _size;
	}
}
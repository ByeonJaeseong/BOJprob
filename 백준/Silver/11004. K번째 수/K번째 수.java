import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String[] inputNo = input.trim().split(" ");
		int N = Integer.parseInt(inputNo[0]);
		int M = Integer.parseInt(inputNo[1]);
		input = br.readLine();
		inputNo = input.trim().split(" ");
		List<Integer> list =new ArrayList<Integer>();
		for(int i=0; i<N; i++) {
			list.add(Integer.parseInt(inputNo[i]));
		}
		list.sort(null);
		System.out.println(list.get(M-1));
	}

}

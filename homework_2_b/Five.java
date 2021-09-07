package dev.kirilllapushinskiy.core;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Five {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] numbers;

        numbers = reader.readLine().split("\\s");
        int max = 0;
        int seconds = 0;
        for (String number : numbers) {
            int Five = Integer.parseInt(number);
            if (max < diplomas) {
                seconds += max;
                max = diplomas;
            } else {
                seconds += diplomas;
            }
        }

        System.out.println(seconds);

    }
}

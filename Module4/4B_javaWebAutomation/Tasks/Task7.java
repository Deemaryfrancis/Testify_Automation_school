package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task7 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url
        driver.get("https://worldweather.wmo.int/en/home.html");
        Thread.sleep(3000);
        driver.findElement(By.name("query")).sendKeys("Abuja");
        Thread.sleep(1000);
        driver.findElement(By.name("submit")).click();
        Thread.sleep(3000);

        //Get Text Attribute
        String text =  driver.findElement(By.cssSelector("div[class*='city_fc_']")).getText();
        System.out.println(text);

        driver.close();
    }
}

package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;

public class Task13 {

    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url - draggable
        driver.get("https://selenium08.blogspot.com/");

        driver.findElement(By.xpath("//div[contains(text(),'Search')]")).click();
        driver.findElement(By.xpath("//header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]" +
                "/div[1]/form[1]/div[1]/input[1]")).sendKeys("Demo dropdown");
        Thread.sleep(3000);
        driver.findElement(By.xpath("//header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]" +
                "/div[1]/form[1]/div[1]/input[1]")).sendKeys(Keys.ENTER);
        Thread.sleep(3000);
        driver.findElement(By.xpath("//body/div[1]/div[2]/div[1]/div[1]/div[1]/main[1]/div[2]/div[1]/div[1]" +
                "/article[1]/div[1]/div[2]/div[4]/div[2]/a[1]")).click();

        WebElement country = driver.findElement(By.name("country"));
        Select pick = new Select(country);
        pick.selectByValue("NG");
        Thread.sleep(3000);

        WebElement month = driver.findElement(By.name("Month"));
        Select select = new Select(month);
        select.selectByValue("Jan");
        select.selectByValue("Feb");
        select.selectByValue("Ma");
        Thread.sleep(3000);

        driver.close();
    }
}
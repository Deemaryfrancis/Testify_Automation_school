package pageObjectModel;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SauceProductPage {
    WebDriver Sdriver=null;
    public SauceProductPage(WebDriver driver){
        Sdriver = driver;
        PageFactory.initElements(Sdriver, this);

    }
    @FindBy(xpath = "//button[@id='add-to-cart-sauce-labs-onesie']")
    private WebElement onesie;
    public WebElement getOnesie(){
        return onesie;
    }
    @FindBy(xpath = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    private WebElement fleece;
    public WebElement getFleece(){
        return fleece;
    }
    @FindBy(xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']")
    private WebElement bikeLight;
    public WebElement getBikeLight(){
        return bikeLight;
    }
}

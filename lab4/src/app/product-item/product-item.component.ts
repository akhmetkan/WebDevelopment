import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent  {

  products = products;

  share(link,description) {
    let ur = "https://t.me/share/url?url=" + link + "&text" + description;
    window.open(ur, "_blank");
  }
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

}

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';

//AIzaSyABvsKu6o9LAdsFM3IqbK-_eKz7ZxdCN_Y

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));

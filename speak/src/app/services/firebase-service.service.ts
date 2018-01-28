import { Injectable } from '@angular/core';
import { AngularFireAuth} from 'angularfire2/auth';
import * as firebase from 'firebase/app';
import { PlofileInfo } from '../models/plofile-info';

@Injectable()
export class FirebaseService {
  constructor(private afauth: AngularFireAuth) { }

  loginWithFacebook(): Promise<PlofileInfo> {

    const provider = new firebase.auth.FacebookAuthProvider();
    return this.afauth.auth.signInWithPopup(provider);
  }
}

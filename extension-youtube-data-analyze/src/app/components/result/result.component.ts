import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  Output,
} from '@angular/core';
import { TranslocoModule } from '@ngneat/transloco';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzResultModule } from 'ng-zorro-antd/result';
@Component({
  selector: 'app-result',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, TranslocoModule, NzResultModule, NzButtonModule],
  styleUrls: ['./result.component.scss'],
  template: `
    <nz-result
      nzStatus="success"
      nzTitle="{{ 'success.msg001' | transloco }}"
      nzSubTitle="{{ 'success.msg002' | transloco }}"
    >
      <div nz-result-extra>
        <button
          (click)="newSearch.emit()"
          nz-button
          nzType="primary"
          nzShape="round"
          nzSize="large"
        >
          {{ 'labels.msg004' | transloco }}
        </button>
      </div>
    </nz-result>
  `,
})
export class ResultComponent {
  @Output() newSearch = new EventEmitter<void>();
}
